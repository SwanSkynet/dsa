"""
Data models for LeetCode problems.

This module defines the core data structures used throughout the application.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class CodeSnippet:
    """Represents a code snippet in a specific programming language."""
    lang: str
    lang_slug: str
    code: str


@dataclass
class TopicTag:
    """Represents a topic tag for a problem."""
    name: str
    slug: str


@dataclass
class Example:
    """Represents a structured example from the problem description."""
    input: str = ""
    output: str = ""
    explanation: str = ""


@dataclass
class TestCase:
    """Represents a single test case."""
    id: int
    inputs: Optional[List[str]]
    expected: str
    explanation: str = ""


@dataclass
class Problem:
    """Represents a complete LeetCode problem with all metadata."""
    question_id: str
    question_frontend_id: str
    title: str
    title_slug: str
    difficulty: str
    content: str
    example_testcases: str
    code_snippets: List[CodeSnippet] = field(default_factory=list)
    topic_tags: List[TopicTag] = field(default_factory=list)
    
    @property
    def url(self) -> str:
        """Get the LeetCode URL for this problem."""
        return f"https://leetcode.com/problems/{self.title_slug}/"
