"""
File system utilities for managing LeetCode solution files.

This module handles all file system operations including directory
creation, filename generation, and file existence checks.
"""

import os
from pathlib import Path
from typing import Tuple


def get_output_directory(difficulty: str, base_path: str = None) -> str:
    """
    Get the output directory path based on problem difficulty.
    
    Args:
        difficulty: Problem difficulty ('Easy', 'Medium', or 'Hard')
        base_path: Base directory path (defaults to script directory)
        
    Returns:
        Full path to output directory
    """
    if base_path is None:
        # Use the parent directory of utils (which is dsa/)
        base_path = Path(__file__).parent.parent
    else:
        base_path = Path(base_path)
    
    problems_dir = base_path / "problems"
    
    difficulty_map = {
        "Easy": problems_dir / "easy",
        "Medium": problems_dir / "medium",
        "Hard": problems_dir / "hard"
    }
    
    return str(difficulty_map.get(difficulty, problems_dir / "medium"))


def generate_filename(problem_number: str, problem_slug: str, language: str) -> str:
    """
    Generate filename for the problem.
    
    Args:
        problem_number: Problem number (e.g., '1')
        problem_slug: Problem slug (e.g., 'two-sum')
        language: Programming language ('python3' or 'cpp')
        
    Returns:
        Filename string (e.g., '1-two-sum.py')
    """
    # Determine file extension
    ext = '.py' if language == 'python3' else '.cpp'
    
    # Create filename
    filename = f"{problem_number}-{problem_slug}{ext}"
    
    return filename


def ensure_directory_exists(directory: str) -> None:
    """
    Ensure that a directory exists, creating it if necessary.
    
    Args:
        directory: Directory path
    """
    os.makedirs(directory, exist_ok=True)


def check_file_exists(file_path: str) -> bool:
    """
    Check if a file exists.
    
    Args:
        file_path: Full file path
        
    Returns:
        True if file exists, False otherwise
    """
    return os.path.exists(file_path)


def prompt_overwrite(filename: str) -> bool:
    """
    Prompt user to confirm file overwrite.
    
    Args:
        filename: Name of the file to overwrite
        
    Returns:
        True if user confirms, False otherwise
    """
    response = input(f"\n⚠️  File already exists: {filename}\nOverwrite? (y/n): ").lower()
    return response == 'y'


def get_full_path(problem_number: str, problem_slug: str, difficulty: str, language: str) -> Tuple[str, str]:
    """
    Get full file path for a problem.
    
    Args:
        problem_number: Problem number
        problem_slug: Problem slug
        difficulty: Problem difficulty
        language: Programming language
        
    Returns:
        Tuple of (filename, full_path)
    """
    filename = generate_filename(problem_number, problem_slug, language)
    directory = get_output_directory(difficulty)
    ensure_directory_exists(directory)
    full_path = os.path.join(directory, filename)
    
    return filename, full_path
