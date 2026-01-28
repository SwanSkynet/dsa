"""
Python solution file generator.

This module generates Python solution files with executable test cases.
"""

import re
from typing import List, Optional
from ..models import Problem, TestCase
from ..parsers import (
    clean_html, extract_examples, extract_constraints,
    parse_structured_examples, extract_function_parameters,
    parse_test_case_string, group_test_inputs, infer_method_name_from_title
)
from ..api_client import LeetCodeAPIClient
from .base import BaseGenerator


class PythonGenerator(BaseGenerator):
    """Generator for creating Python solution files."""
    
    def __init__(self, api_client: LeetCodeAPIClient):
        """
        Initialize the Python generator.
        
        Args:
            api_client: LeetCode API client instance
        """
        self.api_client = api_client
    
    def get_file_extension(self) -> str:
        """Return the file extension for Python files."""
        return '.py'
    
    def generate_file(self, problem: Problem, file_path: str) -> None:
        """
        Generate a Python solution file.
        
        Args:
            problem: Problem object with all details
            file_path: Full path where file should be created
        """
        # Clean and parse content
        content = clean_html(problem.content)
        examples_text = extract_examples(content)
        constraints = extract_constraints(content)
        structured_examples = parse_structured_examples(content)
        
        # Get starter code
        starter_code = self.api_client.get_starter_code(problem, 'python3')
        
        # Extract method information
        if starter_code:
            method_match = re.search(r'def (\w+)\s*\(', starter_code)
            method_name = method_match.group(1) if method_match else infer_method_name_from_title(problem.title)
            
            # Ensure the method has a body (add pass if empty)
            if starter_code.strip().endswith(':'):
                solution_class = starter_code + '\n        pass'
            else:
                # Check if method body is empty (only whitespace after the colon)
                lines = starter_code.split('\n')
                if len(lines) > 0:
                    last_line = lines[-1]
                    if last_line.strip() == '' or ':' in lines[-2] if len(lines) > 1 else False:
                        solution_class = starter_code.rstrip() + '\n        pass'
                    else:
                        solution_class = starter_code
                else:
                    solution_class = starter_code
            
            param_names = extract_function_parameters(starter_code)
        else:
            method_name = infer_method_name_from_title(problem.title)
            param_names = []
            solution_class = f"""class Solution:
    def {method_name}(self):
        \"\"\"
        TODO: Add parameters based on the problem requirements.
        Example: def {method_name}(self, nums: List[int], target: int) -> List[int]:
        \"\"\"
        # TODO: Implement your solution here
        pass"""
        
        # Generate test cases
        test_cases = self._generate_test_cases(
            problem.example_testcases,
            structured_examples,
            param_names
        )
        
        # Format documentation sections
        example_text = self.format_examples(examples_text)
        constraint_text = self.format_constraints(constraints)
        description = self.get_description(content)
        
        # Create param list for documentation
        param_names_str = repr(param_names)
        
        # Generate complete file content
        template = self._create_template(
            problem=problem,
            description=description,
            example_text=example_text,
            constraint_text=constraint_text,
            solution_class=solution_class,
            method_name=method_name,
            param_names_str=param_names_str,
            test_cases=test_cases
        )
        
        # Write to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(template)
    
    def _generate_test_cases(
        self,
        example_testcases: str,
        structured_examples: List,
        param_names: List[str]
    ) -> str:
        """
        Generate test cases code section.
        
        Args:
            example_testcases: Raw test cases from LeetCode
            structured_examples: Parsed examples with input/output
            param_names: Parameter names from function signature
            
        Returns:
            Formatted test cases string
        """
        test_cases = ""
        
        if example_testcases and param_names:
            # Parse and group test cases
            test_lines = parse_test_case_string(example_testcases)
            grouped_inputs = group_test_inputs(test_lines, len(param_names))
            
            # Match with structured examples for expected outputs
            for i, (input_group, example) in enumerate(zip(grouped_inputs, structured_examples), 1):
                output_str = example.output.replace('\n', ' ')
                explanation = example.explanation.replace('\n', ' ')
                
                test_cases += f"""        {{
            'id': {i},
            'inputs': {repr(input_group)},
            'expected': {repr(output_str)},
            'explanation': {repr(explanation)}
        }},
"""
        elif structured_examples:
            # Fallback: use structured examples without actual test data
            for i, example in enumerate(structured_examples, 1):
                output_str = example.output.replace('\n', ' ')
                explanation = example.explanation.replace('\n', ' ')
                
                test_cases += f"""        {{
            'id': {i},
            'inputs': None,  # TODO: Add test inputs manually
            'expected': {repr(output_str)},
            'explanation': {repr(explanation)}
        }},
"""
        else:
            test_cases = """        # TODO: Add test cases manually
        # Example format:
        # {
        #     'id': 1,
        #     'inputs': ['[2,7,11,15]', '9'],
        #     'expected': '[0,1]',
        #     'explanation': 'nums[0] + nums[1] == 9'
        # },
"""
        
        return test_cases
    
    def _create_template(
        self,
        problem: Problem,
        description: str,
        example_text: str,
        constraint_text: str,
        solution_class: str,
        method_name: str,
        param_names_str: str,
        test_cases: str
    ) -> str:
        """
        Create the complete Python file template.
        
        Args:
            problem: Problem object
            description: Formatted description
            example_text: Formatted examples
            constraint_text: Formatted constraints
            solution_class: Solution class code
            method_name: Name of the solution method
            param_names_str: String representation of parameter names list
            test_cases: Formatted test cases
            
        Returns:
            Complete file content
        """
        return f'''\"\"\"\nProblem: {problem.title}
LeetCode: #{problem.question_frontend_id}
Difficulty: {problem.difficulty}
Link: {problem.url}

Description:
{description}

Examples:
{example_text}

Constraints:
{constraint_text}

Time Complexity: O(?)
Space Complexity: O(?)

Approach:
TODO: Explain your approach here
\"\"\"

from typing import List, Optional
import json


{solution_class}


def parse_input(input_str: str):
    \"\"\"Parse a JSON-like input string to Python object.\"\"\"
    try:
        return json.loads(input_str)
    except:
        # If JSON parsing fails, try to evaluate as Python literal
        try:
            import ast
            return ast.literal_eval(input_str)
        except:
            # Return as-is if all parsing fails
            return input_str


def run_tests():
    \"\"\"Run all test cases and display results like LeetCode.\"\"\"
    solution = Solution()
    param_names = {param_names_str}
    test_cases = [
{test_cases}    ]
    
    print("=" * 60)
    print(f"Running {{len(test_cases)}} test case(s)...")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for test in test_cases:
        test_id = test['id']
        inputs = test.get('inputs')
        expected = test['expected']
        
        print(f"\\n📝 Test {{test_id}}:")
        
        if inputs is None:
            print("⚠️  Test inputs not available. Please add them manually.")
            continue
        
        # Parse inputs
        try:
            parsed_inputs = [parse_input(inp) for inp in inputs]
            # Display input parameters
            if param_names:
                input_display = [f"{{name}}={{val}}" for name, val in zip(param_names, parsed_inputs)]
                print(f"Input: {{', '.join(input_display)}}")
            else:
                print(f"Input: {{parsed_inputs}}")
        except Exception as e:
            print(f"❌ Error parsing inputs: {{e}}")
            failed += 1
            continue
        
        print(f"Expected: {{expected}}")
        
        try:
            # Call solution method with parsed inputs
            result = solution.{method_name}(*parsed_inputs)
            print(f"Got: {{result}}")
            
            # Parse expected output for comparison
            try:
                expected_parsed = parse_input(expected)
            except:
                expected_parsed = expected
            
            # Compare result with expected
            if result == expected_parsed or str(result) == expected:
                print("✅ PASS")
                passed += 1
            else:
                print("❌ FAIL")
                failed += 1
            
        except NotImplementedError:
            print("⚠️  Solution not implemented yet")
        except Exception as e:
            print(f"❌ ERROR: {{e}}")
            import traceback
            traceback.print_exc()
            failed += 1
        
        if test.get('explanation'):
            print(f"💡 Explanation: {{test['explanation']}}")
    
    print("\\n" + "=" * 60)
    print(f"Results: {{passed}} passed, {{failed}} failed, {{len(test_cases)}} total")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
'''
