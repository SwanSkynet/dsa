# 🚀 Data Structures & Algorithms

A comprehensive collection of LeetCode problems and DSA implementations organized by difficulty, data structures, and algorithmic patterns.

## 📁 Repository Structure

```
dsa/
├── create_problem.py         # Main problem generator script
│
├── leetcode/                 # Problem generation modules (scripts only)
│   ├── api_client.py        # LeetCode API client
│   ├── models.py            # Data models
│   ├── parsers.py           # Content parsers
│   └── generators/          # Language-specific generators
│       ├── base.py          # Abstract base generator
│       ├── python.py        # Python file generator
│       └── cpp.py           # C++ file generator
│
├── utils/                    # Utility modules (scripts only)
│   └── file_utils.py        # File system operations
│
├── problems/                 # Generated LeetCode solutions ⭐
│   ├── easy/                # Easy level problems
│   ├── medium/              # Medium level problems
│   └── hard/                # Hard level problems
│
├── data-structures/          # Data structure implementations and related problems
│   ├── arrays/              # Array problems and implementations
│   ├── linked-lists/        # Linked list problems and implementations
│   ├── trees/               # Binary trees, BST, AVL, etc.
│   ├── graphs/              # Graph algorithms and problems
│   ├── stacks-queues/       # Stack and Queue implementations
│   ├── hash-tables/         # Hash map and set problems
│   └── heaps/               # Heap and priority queue problems
│
└── algorithms/               # Algorithm patterns and techniques
    ├── sorting/             # Various sorting algorithms
    ├── searching/           # Binary search and variations
    ├── dynamic-programming/ # DP problems and patterns
    ├── greedy/              # Greedy algorithm problems
    ├── backtracking/        # Backtracking problems
    └── divide-conquer/      # Divide and conquer approaches
```

> **Note:** The `leetcode/` and `utils/` directories contain code generation scripts and modules. All generated problem files are placed in the `problems/` directory.

## 🤖 Quick Start - Automated File Creation

Use the automated script to create problem files quickly:

```bash
# Install dependencies (first time only)
pip install -r requirements.txt

# Run the script
python3 create_problem.py
```

The script will:

1. Ask for the LeetCode problem URL
2. Ask for your preferred language (Python3 or C++)
3. Fetch problem details from LeetCode
4. Generate a properly formatted file with the problem description
5. Automatically place it in the correct difficulty folder

**Example:**

```
📎 Enter LeetCode problem URL: https://leetcode.com/problems/two-sum/description/
💻 Select language:
  1. Python3
  2. C++
Enter choice (1 or 2): 1

✅ Created: problems/easy/1-two-sum.py
```

## 📝 File Naming Convention

Each solution file follows this pattern:

```
<problem-number>-<problem-name>.<extension>
```

**Examples:**

- `1-two-sum.py`
- `15-3sum.js`
- `206-reverse-linked-list.cpp`

## 📋 Problem Template

Each problem solution should include:

```python
"""
Problem: <Problem Name>
LeetCode: <Problem Number>
Difficulty: <Easy/Medium/Hard>
Link: <LeetCode URL>

Description:
<Brief problem description>

Examples:
Input: <example input>
Output: <example output>

Constraints:
- <constraint 1>
- <constraint 2>

Time Complexity: O(?)
Space Complexity: O(?)

Approach:
<Brief explanation of the approach>
"""

# Solution code here
```

## 🎯 Progress Tracking

| Difficulty | Solved | Total   |
| ---------- | ------ | ------- |
| Easy       | 0      | TBD     |
| Medium     | 0      | TBD     |
| Hard       | 0      | TBD     |
| **Total**  | **0**  | **TBD** |

## 📚 Topics Covered

### Data Structures

- [ ] Arrays & Strings
- [ ] Linked Lists
- [ ] Stacks & Queues
- [ ] Trees & Binary Search Trees
- [ ] Heaps & Priority Queues
- [ ] Hash Tables
- [ ] Graphs
- [ ] Tries
- [ ] Union Find

### Algorithms

- [ ] Two Pointers
- [ ] Sliding Window
- [ ] Binary Search
- [ ] Sorting Algorithms
- [ ] Dynamic Programming
- [ ] Greedy Algorithms
- [ ] Backtracking
- [ ] Depth-First Search (DFS)
- [ ] Breadth-First Search (BFS)
- [ ] Divide and Conquer

## 🏆 Study Plan

### Phase 1: Foundations

- Arrays & Hashing
- Two Pointers
- Sliding Window
- Stack

### Phase 2: Core Data Structures

- Linked Lists
- Binary Trees
- Binary Search Trees
- Heaps

### Phase 3: Advanced Patterns

- Graphs (DFS/BFS)
- Dynamic Programming
- Backtracking
- Greedy Algorithms

### Phase 4: Advanced Topics

- Advanced Graph Algorithms
- Advanced DP
- Bit Manipulation
- Math & Geometry

## 📖 Resources

- [LeetCode](https://leetcode.com/)
- [NeetCode Roadmap](https://neetcode.io/roadmap)
- [Blind 75](https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU)
- [Grind 75](https://www.techinterviewhandbook.org/grind75)

## 💡 Tips for Success

1. **Understand Before Coding**: Always understand the problem completely before writing code
2. **Start with Brute Force**: Think of the simplest solution first, then optimize
3. **Test with Examples**: Run through examples manually before submitting
4. **Time Yourself**: Practice under time constraints for interview prep
5. **Review and Revise**: Revisit problems after a few days/weeks

## 🔧 Languages Used

- Python
- JavaScript/TypeScript
- C++
- Java
- Go

## 📝 Notes

- Each solution includes detailed comments explaining the approach
- Time and space complexity analysis included
- Multiple solutions provided when applicable (brute force → optimized)
- Test cases included in comments

## 📫 Contact

Feel free to reach out for discussions or suggestions!

---

**Last Updated**: January 2026
