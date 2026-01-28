"""
Base generator class for creating LeetCode solution files.

This module defines the abstract base class that all language-specific
generators must inherit from.
"""

from abc import ABC, abstractmethod
from typing import List
from ..models import Problem, Example


class BaseGenerator(ABC):
    """Abstract base class for language-specific file generators."""
    
    @abstractmethod
    def generate_file(self, problem: Problem, file_path: str) -> None:
        """
        Generate a solution file for the given problem.
        
        Args:
            problem: Problem object with all details
            file_path: Full path where file should be created
        """
        pass
    
    @abstractmethod
    def get_file_extension(self) -> str:
        """
        Get the file extension for this language.
        
        Returns:
            File extension (e.g., '.py', '.cpp')
        """
        pass
    
    def format_examples(self, examples: List[str], max_length: int = 500) -> str:
        """
        Format examples for documentation.
        
        Args:
            examples: List of example strings
            max_length: Maximum length of formatted output
            
        Returns:
            Formatted examples string
        """
        if not examples:
            return "See problem description"
        
        formatted = '\n\n'.join(examples)
        
        # Truncate if too long
        if len(formatted) > max_length:
            formatted = formatted[:max_length]
        
        return formatted
    
    def format_constraints(self, constraints: List[str]) -> str:
        """
        Format constraints for documentation.
        
        Args:
            constraints: List of constraint strings
            
        Returns:
            Formatted constraints string
        """
        if not constraints:
            return "- See problem description"
        
        return '\n'.join([f"- {c}" for c in constraints])
    
    def get_description(self, content: str, max_length: int = 500) -> str:
        """
        Extract and format problem description.
        
        Args:
            content: Full problem content
            max_length: Maximum length of description
            
        Returns:
            Formatted description
        """
        # Get description (before examples)
        description = content.split("Example")[0].strip() if "Example" in content else content
        
        # Truncate if too long
        if len(description) > max_length:
            description = description[:max_length]
        
        return description
