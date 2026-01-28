#!/usr/bin/env python3
"""
LeetCode Problem File Generator - CLI Entry Point

This script automates the creation of LeetCode solution files by:
1. Fetching problem details from LeetCode
2. Generating properly formatted solution files with executable test cases
3. Organizing them by difficulty
"""

import sys
from leetcode import LeetCodeAPIClient
from leetcode.generators import PythonGenerator, CppGenerator
from utils import get_full_path, check_file_exists, prompt_overwrite


def main():
    """Main entry point for the CLI."""
    print("=" * 60)
    print("🚀 LeetCode Problem File Generator")
    print("=" * 60)
    
    # Initialize API client
    api_client = LeetCodeAPIClient()
    
    # Get URL from user
    url = input("\n📎 Enter LeetCode problem URL: ").strip()
    
    if not url:
        print("❌ Error: URL cannot be empty")
        sys.exit(1)
    
    print(f"\n🔍 Processing URL: {url}")
    
    # Extract slug
    slug = api_client.extract_slug_from_url(url)
    if not slug:
        print("❌ Error: Invalid LeetCode URL")
        sys.exit(1)
    
    print(f"📝 Problem slug: {slug}")
    
    # Fetch problem details
    print("🌐 Fetching problem details from LeetCode...")
    problem = api_client.fetch_problem(slug)
    
    if not problem:
        print("❌ Error: Could not fetch problem details")
        sys.exit(1)
    
    print(f"✅ Found: {problem.title} (#{problem.question_frontend_id})")
    print(f"📊 Difficulty: {problem.difficulty}")
    
    # Get language from user
    print("\n💻 Select language:")
    print("  1. Python3")
    print("  2. C++")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    language_map = {
        '1': 'python3',
        '2': 'cpp'
    }
    
    language = language_map.get(choice)
    
    if not language:
        print("❌ Error: Invalid language choice")
        sys.exit(1)
    
    # Generate filename and path
    filename, file_path = get_full_path(
        problem.question_frontend_id,
        problem.title_slug,
        problem.difficulty,
        language
    )
    
    # Check if file already exists
    if check_file_exists(file_path):
        if not prompt_overwrite(filename):
            print("❌ Cancelled")
            sys.exit(0)
    
    # Generate file based on language
    print(f"\n📝 Generating {language} solution file...")
    
    try:
        if language == 'python3':
            generator = PythonGenerator(api_client)
        elif language == 'cpp':
            generator = CppGenerator(api_client)
        else:
            print(f"❌ Error: Unsupported language: {language}")
            sys.exit(1)
        
        generator.generate_file(problem, file_path)
        
        print(f"✅ Created: {file_path}")
        print(f"\n🎯 File created successfully!")
        print(f"📂 Location: {file_path}")
        print(f"\n💡 Tip: Run the file to execute test cases automatically!")
        
        if language == 'python3':
            print(f"   python3 {filename}")
        else:
            print(f"   g++ {filename} -o solution && ./solution")
        
        # Show topics
        if problem.topic_tags:
            topics = [tag.name for tag in problem.topic_tags]
            print(f"\n🏷️  Topics: {', '.join(topics)}")
        
        print("\n✨ Happy coding! 🎉")
        
    except Exception as e:
        print(f"\n❌ Error generating file: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
