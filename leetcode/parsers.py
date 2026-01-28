"""
Content parsing utilities for LeetCode problems.

This module provides functions to parse and extract information from
problem descriptions, including HTML cleaning, example extraction, and
test case parsing.
"""

import re
from typing import List, Dict, Tuple
from .models import Example


def clean_html(html_content: str) -> str:
    """
    Remove HTML tags and format the content.
    
    Args:
        html_content: Raw HTML content from LeetCode
        
    Returns:
        Cleaned text content
    """
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', html_content)
    
    # Decode HTML entities
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&quot;', '"')
    text = text.replace('&#39;', "'")
    text = text.replace('&amp;', '&')
    
    # Clean up whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    return text.strip()


def extract_examples(content: str) -> List[str]:
    """
    Extract example sections from problem content.
    
    Args:
        content: Cleaned problem content
        
    Returns:
        List of example strings
    """
    examples = []
    
    # Extract examples
    example_pattern = r'Example \d+:.*?(?=Example \d+:|Constraints:|$)'
    example_matches = re.findall(example_pattern, content, re.DOTALL)
    
    for match in example_matches:
        examples.append(match.strip())
    
    return examples


def extract_constraints(content: str) -> List[str]:
    """
    Extract constraints from problem content.
    
    Args:
        content: Cleaned problem content
        
    Returns:
        List of constraint strings
    """
    constraints = []
    
    # Extract constraints
    constraint_pattern = r'Constraints:(.*?)(?=\n\n[A-Z]|$)'
    constraint_match = re.search(constraint_pattern, content, re.DOTALL)
    
    if constraint_match:
        constraint_text = constraint_match.group(1).strip()
        constraints = [c.strip() for c in constraint_text.split('\n') if c.strip()]
    
    return constraints


def parse_structured_examples(content: str) -> List[Example]:
    """
    Extract structured examples with inputs, outputs, and explanations.
    
    Args:
        content: Cleaned problem content
        
    Returns:
        List of Example objects
    """
    examples = []
    
    # Pattern to match Example sections
    example_pattern = r'Example \d+:(.*?)(?=Example \d+:|Constraints:|$)'
    example_matches = re.findall(example_pattern, content, re.DOTALL | re.IGNORECASE)
    
    for match in example_matches:
        example_data = {}
        
        # Extract Input
        input_match = re.search(r'Input:\s*(.+?)(?=Output:|$)', match, re.DOTALL | re.IGNORECASE)
        if input_match:
            example_data['input'] = input_match.group(1).strip()
        
        # Extract Output
        output_match = re.search(r'Output:\s*(.+?)(?=Explanation:|Example|$)', match, re.DOTALL | re.IGNORECASE)
        if output_match:
            example_data['output'] = output_match.group(1).strip()
        
        # Extract Explanation (optional)
        explanation_match = re.search(r'Explanation:\s*(.+?)(?=Example|$)', match, re.DOTALL | re.IGNORECASE)
        if explanation_match:
            example_data['explanation'] = explanation_match.group(1).strip()
        
        if example_data.get('input') or example_data.get('output'):
            examples.append(Example(**example_data))
    
    return examples


def parse_input_parameters(input_str: str) -> Dict[str, str]:
    """
    Parse input string to extract parameter names and values.
    
    Args:
        input_str: Input string in format "param1 = value1, param2 = value2"
        
    Returns:
        Dictionary mapping parameter names to values
    """
    params = {}
    # Match pattern like: param1 = value1, param2 = value2
    param_pattern = r'(\w+)\s*=\s*(.+?)(?=,\s*\w+\s*=|$)'
    matches = re.findall(param_pattern, input_str)
    
    for param_name, param_value in matches:
        params[param_name.strip()] = param_value.strip()
    
    return params


def infer_method_name_from_title(title: str) -> str:
    """
    Infer method name from problem title (convert to camelCase).
    
    Args:
        title: Problem title (e.g., "Two Sum")
        
    Returns:
        Method name in camelCase (e.g., "twoSum")
    """
    # Convert title to camelCase
    words = re.findall(r'\w+', title)
    if not words:
        return "solve"
    
    # First word lowercase, rest capitalized
    method_name = words[0].lower() + ''.join(w.capitalize() for w in words[1:])
    return method_name


def extract_function_parameters(starter_code: str) -> List[str]:
    """
    Extract parameter names from the function signature in starter code.
    
    Args:
        starter_code: Starter code containing function definition
        
    Returns:
        List of parameter names (excluding 'self')
    """
    # Match function definition like: def functionName(self, param1: Type1, param2: Type2) -> ReturnType:
    match = re.search(r'def\s+\w+\s*\(([^)]*)\)', starter_code)
    if not match:
        return []
    
    params_str = match.group(1)
    params = []
    
    # Split by comma and extract parameter names
    for param in params_str.split(','):
        param = param.strip()
        if not param or param == 'self':
            continue
        # Extract just the parameter name (before : or =)
        param_name = re.split(r'[:\s=]', param)[0].strip()
        if param_name:
            params.append(param_name)
    
    return params


def parse_test_case_string(test_cases_str: str) -> List[str]:
    """
    Parse the exampleTestcases string into individual test input lines.
    
    Args:
        test_cases_str: Raw test cases string from LeetCode API
        
    Returns:
        List of test input lines
    """
    if not test_cases_str:
        return []
    
    # Split by newline - each line is a separate input parameter
    lines = [line.strip() for line in test_cases_str.strip().split('\n') if line.strip()]
    
    return lines


def group_test_inputs(test_lines: List[str], num_params: int) -> List[List[str]]:
    """
    Group test input lines by number of parameters.
    
    Args:
        test_lines: List of individual test input lines
        num_params: Number of parameters per test case
        
    Returns:
        List of test cases, where each test case is a list of inputs
    """
    if num_params <= 0:
        return [[line] for line in test_lines]
    
    grouped = []
    for i in range(0, len(test_lines), num_params):
        group = test_lines[i:i + num_params]
        if len(group) == num_params:
            grouped.append(group)
    
    return grouped
