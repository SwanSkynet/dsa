"""
LeetCode API client for fetching problem details.

This module handles all interactions with the LeetCode GraphQL API.
"""

import re
import requests
from typing import Optional
from .models import Problem, CodeSnippet, TopicTag


class LeetCodeAPIClient:
    """Client for interacting with the LeetCode GraphQL API."""
    
    def __init__(self):
        """Initialize the API client with default configuration."""
        self.base_url = "https://leetcode.com"
        self.graphql_url = "https://leetcode.com/graphql"
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        }
        self.timeout = 10
    
    def extract_slug_from_url(self, url: str) -> Optional[str]:
        """
        Extract problem slug from LeetCode URL.
        
        Args:
            url: Full LeetCode problem URL
            
        Returns:
            Problem slug or None if not found
            
        Examples:
            >>> client = LeetCodeAPIClient()
            >>> client.extract_slug_from_url("https://leetcode.com/problems/two-sum/")
            'two-sum'
        """
        pattern = r'leetcode\.com/problems/([^/]+)'
        match = re.search(pattern, url)
        return match.group(1) if match else None
    
    def fetch_problem(self, slug: str) -> Optional[Problem]:
        """
        Fetch complete problem details from LeetCode GraphQL API.
        
        Args:
            slug: Problem slug (e.g., 'two-sum')
            
        Returns:
            Problem object or None if fetch fails
        """
        query = """
        query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                title
                titleSlug
                difficulty
                content
                exampleTestcases
                codeSnippets {
                    lang
                    langSlug
                    code
                }
                topicTags {
                    name
                    slug
                }
            }
        }
        """
        
        payload = {
            "query": query,
            "variables": {"titleSlug": slug}
        }
        
        try:
            response = requests.post(
                self.graphql_url,
                json=payload,
                headers=self.headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            data = response.json()
            
            if 'data' in data and data['data']['question']:
                question_data = data['data']['question']
                return self._parse_problem_response(question_data)
            
            return None
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching problem details: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    def _parse_problem_response(self, data: dict) -> Problem:
        """
        Parse GraphQL response into Problem object.
        
        Args:
            data: Raw response data from GraphQL API
            
        Returns:
            Problem object
        """
        # Parse code snippets
        code_snippets = [
            CodeSnippet(
                lang=snippet['lang'],
                lang_slug=snippet['langSlug'],
                code=snippet['code']
            )
            for snippet in data.get('codeSnippets', [])
        ]
        
        # Parse topic tags
        topic_tags = [
            TopicTag(
                name=tag['name'],
                slug=tag['slug']
            )
            for tag in data.get('topicTags', [])
        ]
        
        return Problem(
            question_id=data['questionId'],
            question_frontend_id=data['questionFrontendId'],
            title=data['title'],
            title_slug=data['titleSlug'],
            difficulty=data['difficulty'],
            content=data['content'],
            example_testcases=data.get('exampleTestcases', ''),
            code_snippets=code_snippets,
            topic_tags=topic_tags
        )
    
    def get_starter_code(self, problem: Problem, language: str) -> Optional[str]:
        """
        Extract starter code for the specified language.
        
        Args:
            problem: Problem object
            language: Language slug ('python3' or 'cpp')
            
        Returns:
            Starter code string or None if not found
        """
        for snippet in problem.code_snippets:
            if snippet.lang_slug == language:
                return snippet.code
        
        return None
