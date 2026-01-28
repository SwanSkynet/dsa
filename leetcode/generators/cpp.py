"""
C++ solution file generator.

This module generates C++ solution files with test case templates.
"""

import re
from typing import List
from ..models import Problem
from ..parsers import (
    clean_html, extract_examples, extract_constraints,
    parse_structured_examples, parse_input_parameters,
    parse_test_case_string, infer_method_name_from_title
)
from ..api_client import LeetCodeAPIClient
from .base import BaseGenerator


class CppGenerator(BaseGenerator):
    """Generator for creating C++ solution files."""
    
    def __init__(self, api_client: LeetCodeAPIClient):
        """
        Initialize the C++ generator.
        
        Args:
            api_client: LeetCode API client instance
        """
        self.api_client = api_client
    
    def get_file_extension(self) -> str:
        """Return the file extension for C++ files."""
        return '.cpp'
    
    def generate_file(self, problem: Problem, file_path: str) -> None:
        """
        Generate a C++ solution file.
        
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
        starter_code = self.api_client.get_starter_code(problem, 'cpp')
        
        # Extract method information
        if starter_code:
            solution_class = starter_code
            method_match = re.search(r'\s+(\w+)\s*\(', starter_code)
            method_name = method_match.group(1) if method_match else infer_method_name_from_title(problem.title)
        else:
            method_name = infer_method_name_from_title(problem.title)
            solution_class = f"""class Solution {{
public:
    // TODO: Implement your solution here
    // Update return type and parameters based on problem requirements
    // Example: vector<int> {method_name}(vector<int>& nums, int target)
    void {method_name}() {{
        
    }}
}};"""
        
        # Generate test cases
        test_cases_code = self._generate_test_cases(
            problem.example_testcases,
            structured_examples,
            method_name
        )
        
        # Format documentation sections
        example_text = self.format_examples(examples_text)
        constraint_text = self.format_constraints(content)
        description = self.get_description(content)
        
        num_tests = len(structured_examples) if structured_examples else 0
        
        # Generate complete file content
        template = self._create_template(
            problem=problem,
            description=description,
            example_text=example_text,
            constraint_text=constraint_text,
            solution_class=solution_class,
            test_cases_code=test_cases_code,
            num_tests=num_tests
        )
        
        # Write to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(template)
    
    def _generate_test_cases(
        self,
        example_testcases: str,
        structured_examples: List,
        method_name: str
    ) -> str:
        """
        Generate test cases code section.
        
        Args:
            example_testcases: Raw test cases from LeetCode
            structured_examples: Parsed examples with input/output
            method_name: Name of the solution method
            
        Returns:
            Formatted test cases string
        """
        test_cases_code = ""
        
        # Parse test case inputs
        test_inputs = []
        if example_testcases:
            test_lines = parse_test_case_string(example_testcases)
            test_inputs = test_lines
        
        if structured_examples:
            for i, example in enumerate(structured_examples, 1):
                # Use actual test input if available
                if i <= len(test_inputs):
                    input_display = test_inputs[i-1]
                else:
                    input_display = example.input.replace('\n', ' ')
                
                output_str = example.output.replace('\n', ' ')
                explanation = example.explanation.replace('\n', ' ')
                
                # Parse parameters for C++
                params = parse_input_parameters(input_display)
                params_display = ', '.join(f'{k} = {v}' for k, v in params.items()) if params else input_display
                
                test_cases_code += f'''
    // Test {i}
    {{
        cout << "\\n📝 Test {i}:" << endl;
        cout << "Input: {params_display}" << endl;
        cout << "Expected: {output_str}" << endl;
        
        // TODO: Parse input values and call solution method
        // Example:
        // vector<int> nums = {{2, 7, 11, 15}};
        // int target = 9;
        // auto result = solution.{method_name}(nums, target);
        
        // Uncomment below after implementing solution
        // cout << "Got: " << result << endl;
        // if (result == expected) {{
        //     cout << "✅ PASS" << endl;
        //     passed++;
        // }} else {{
        //     cout << "❌ FAIL" << endl;
        //     failed++;
        // }}
        
        cout << "⚠️  Not implemented yet" << endl;
'''
                if explanation:
                    test_cases_code += f'        cout << "💡 Explanation: {explanation}" << endl;\n'
                
                test_cases_code += '    }\n'
        else:
            test_cases_code = '''
    // TODO: Add test cases manually
    // Example:
    // {
    //     cout << "\\n📝 Test 1:" << endl;
    //     vector<int> nums = {2, 7, 11, 15};
    //     int target = 9;
    //     auto result = solution.methodName(nums, target);
    //     cout << "Input: nums = [2,7,11,15], target = 9" << endl;
    //     cout << "Expected: [0,1]" << endl;
    //     cout << "Got: [" << result[0] << "," << result[1] << "]" << endl;
    // }
'''
        
        return test_cases_code
    
    def _create_template(
        self,
        problem: Problem,
        description: str,
        example_text: str,
        constraint_text: str,
        solution_class: str,
        test_cases_code: str,
        num_tests: int
    ) -> str:
        """
        Create the complete C++ file template.
        
        Args:
            problem: Problem object
            description: Formatted description
            example_text: Formatted examples
            constraint_text: Formatted constraints
            solution_class: Solution class code
            test_cases_code: Formatted test cases
            num_tests: Number of test cases
            
        Returns:
            Complete file content
        """
        return f'''/**
 * Problem: {problem.title}
 * LeetCode: #{problem.question_frontend_id}
 * Difficulty: {problem.difficulty}
 * Link: {problem.url}
 * 
 * Description:
 * {description}
 * 
 * Examples:
 * {example_text}
 * 
 * Constraints:
 * {constraint_text}
 * 
 * Time Complexity: O(?)
 * Space Complexity: O(?)
 * 
 * Approach:
 * TODO: Explain your approach here
 */

#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <iostream>
using namespace std;

{solution_class}

void runTests() {{
    Solution solution;
    int passed = 0;
    int failed = 0;
    int total = {num_tests};
    
    cout << "============================================================" << endl;
    cout << "Running " << total << " test case(s)..." << endl;
    cout << "============================================================" << endl;
{test_cases_code}
    cout << "\\n============================================================" << endl;
    cout << "Results: " << passed << " passed, " << failed << " failed, " << total << " total" << endl;
    cout << "============================================================" << endl;
}}

int main() {{
    runTests();
    return 0;
}}
'''
