# LeetCode Problem Generator - Usage Guide

## Installation

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests
```

## Usage

### Basic Usage

Run the script:

```bash
python3 create_problem.py
```

The script will prompt you for:

1. **LeetCode URL** - Paste the full problem URL
2. **Language** - Choose between Python3 (1) or C++ (2)

### Example Session

```
============================================================
🚀 LeetCode Problem File Generator
============================================================

📎 Enter LeetCode problem URL: https://leetcode.com/problems/two-sum/description/

💻 Select language:
  1. Python3
  2. C++

Enter choice (1 or 2): 1

🔍 Processing URL: https://leetcode.com/problems/two-sum/description/
📝 Problem slug: two-sum
🌐 Fetching problem details from LeetCode...
✅ Found: Two Sum (#1)
📊 Difficulty: Easy

📝 Generating python3 solution file...
✅ Created: /path/to/problems/easy/1-two-sum.py

🎯 File created successfully!
📂 Location: /path/to/problems/easy/1-two-sum.py
🏷️  Topics: Array, Hash Table

✨ Happy coding! 🎉
```

## Supported URLs

The script accepts various LeetCode URL formats:

- `https://leetcode.com/problems/two-sum/`
- `https://leetcode.com/problems/two-sum/description/`
- `https://leetcode.com/problems/two-sum/solutions/`

## Features

✅ Automatically fetches problem details from LeetCode
✅ Extracts problem number, title, difficulty, description
✅ Includes examples and constraints
✅ Organizes files by difficulty (easy/medium/hard)
✅ Uses proper naming convention
✅ Adds TODO comments for you to fill in
✅ Shows related topics/tags

## File Organization

Files are automatically organized by difficulty:

- Easy problems → `problems/easy/`
- Medium problems → `problems/medium/`
- Hard problems → `problems/hard/`

> **Note:** The `leetcode/` directory contains code generation scripts. All generated problem solutions are saved in the `problems/` directory.

## Generated File Structure

### Python Files

```python
"""
Problem: [Title]
LeetCode: #[Number]
Difficulty: [Easy/Medium/Hard]
Link: [URL]

Description:
[Problem description]

Examples:
[Examples from LeetCode]

Constraints:
[Constraints from LeetCode]

Time Complexity: O(?)
Space Complexity: O(?)

Approach:
TODO: Explain your approach here
"""

class Solution:
    def solve(self):
        # TODO: Implement solution
        pass

# Test cases
if __name__ == "__main__":
    solution = Solution()
    # TODO: Add test cases
    print("All tests passed!")
```

### C++ Files

```cpp
/**
 * Problem: [Title]
 * LeetCode: #[Number]
 * Difficulty: [Easy/Medium/Hard]
 * Link: [URL]
 *
 * Description:
 * [Problem description]
 *
 * Time Complexity: O(?)
 * Space Complexity: O(?)
 */

#include <vector>
// ... standard includes

class Solution {
public:
    void solve() {
        // TODO: Implement solution
    }
};

int main() {
    // TODO: Add test cases
    return 0;
}
```

## Tips

1. **Check if file exists**: The script will warn you if a file already exists and ask if you want to overwrite it

2. **Internet required**: The script needs internet access to fetch problem details from LeetCode

3. **Manual editing**: After generation, you'll need to:
   - Implement the solution
   - Update Time/Space complexity
   - Add your approach explanation
   - Write test cases

## Troubleshooting

### "Invalid LeetCode URL"

Make sure you're using a valid LeetCode problem URL starting with `https://leetcode.com/problems/`

### "Could not fetch problem details"

- Check your internet connection
- Verify the problem exists on LeetCode
- LeetCode might be temporarily unavailable

### "Module 'requests' not found"

Install the required dependency:

```bash
pip install requests
```

## Manual File Creation

If you prefer to create files manually, refer to [TEMPLATE.md](TEMPLATE.md) for the proper format.

## Future Enhancements

Potential features to add:

- Support for more languages (Java, JavaScript, Go, Rust)
- Batch processing of multiple problems
- Integration with LeetCode's contest problems
- Automatic test case generation
- Solution hints and common patterns
