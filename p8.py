from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Your code here
        left = 0
        right = len(height) -1
        max_area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right-left)
            max_area = max(current_area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))  # Expected: 49
    print(solution.maxArea([1,1]))  # Expected: 1


## **Understanding the Problem**

# **Water container area formula:**
# ```
# area = min(height[left], height[right]) * (right - left)
#        └─────────────────┬─────────────┘   └──────┬──────┘
#               water height                    width
# ```

# **Why `min(height[left], height[right])`?**
# - Water level is limited by the **shorter** line
# - Like a bucket - water spills over the shorter side!

# **Visual example:**
# ```
# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#           0  1  2  3  4  5  6  7  8  (indices)

# If we pick lines at index 1 and 8:
# - heights are 8 and 7
# - water height = min(8, 7) = 7
# - width = 8 - 1 = 7
# - area = 7 * 7 = 49