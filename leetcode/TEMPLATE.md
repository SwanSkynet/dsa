# Problem Solution Template

Use this template when adding new LeetCode solutions to maintain consistency.

## File Naming
`<number>-<problem-name>.<ext>`

Example: `1-two-sum.py`

## Code Template (Python)

```python
"""
Problem: Two Sum
LeetCode: #1
Difficulty: Easy
Link: https://leetcode.com/problems/two-sum/

Description:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Time Complexity: O(n)
Space Complexity: O(n)

Approach:
Use a hash map to store values and their indices. For each number, check if 
target - num exists in the map. If yes, return the indices. Otherwise, add 
the current number to the map.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store value -> index mapping
        seen = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in our map
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number and its index
            seen[num] = i
        
        return []  # No solution found

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1
    assert solution.twoSum([2,7,11,15], 9) == [0,1]
    
    # Test 2
    assert solution.twoSum([3,2,4], 6) == [1,2]
    
    # Test 3
    assert solution.twoSum([3,3], 6) == [0,1]
    
    print("All tests passed!")
```

## Code Template (JavaScript)

```javascript
/**
 * Problem: Two Sum
 * LeetCode: #1
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/two-sum/
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * 
 * Approach:
 * Use a hash map to store values and their indices.
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = new Map();
    
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        
        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }
        
        seen.set(nums[i], i);
    }
    
    return [];
};

// Test cases
console.log(twoSum([2,7,11,15], 9)); // [0,1]
console.log(twoSum([3,2,4], 6));     // [1,2]
console.log(twoSum([3,3], 6));       // [0,1]
```

## Code Template (C++)

```cpp
/**
 * Problem: Two Sum
 * LeetCode: #1
 * Difficulty: Easy
 * Link: https://leetcode.com/problems/two-sum/
 * 
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            
            if (seen.find(complement) != seen.end()) {
                return {seen[complement], i};
            }
            
            seen[nums[i]] = i;
        }
        
        return {};
    }
};
```

## Checklist Before Committing

- [ ] Problem description and link included
- [ ] Time and space complexity analyzed
- [ ] Approach explanation provided
- [ ] Code is well-commented
- [ ] Test cases included
- [ ] Edge cases considered
- [ ] File named correctly
- [ ] Placed in correct directory
