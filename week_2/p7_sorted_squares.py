from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        square = 0
        for i in nums:
            square = i ** 2
            result.append(square)
        return sorted(result)
    
    # n = len(nums)
    # result = [0] * n  # Create result array
    # left = 0
    # right = n - 1
    # pos = n - 1  # Fill from the end
    
    # while left <= right:
    #     left_square = nums[left] ** 2
    #     right_square = nums[right] ** 2
        
    #     if left_square > right_square:
    #         result[pos] = left_square
    #         left += 1
    #     else:
    #         result[pos] = right_square
    #         right -= 1
        
    #     pos -= 1
    
    # return result

# Test
solution = Solution()
print(solution.sortedSquares([-4,-1,0,3,10]))  # [0,1,9,16,100]
print(solution.sortedSquares([-7,-3,2,3,11]))  # [4,9,9,49,121]
# ```

# **Problem:** Given a sorted array (with negative and positive numbers), return an array of the squares of each number, also sorted.

# **Examples:**
# ```
# Input:  [-4, -1, 0, 3, 10]
# Squares: [16, 1, 0, 9, 100]
# Sorted:  [0, 1, 9, 16, 100]

# Input:  [-7, -3, 2, 3, 11]
# Squares: [49, 9, 4, 9, 121]
# Sorted:  [4, 9, 9, 49, 121]
# ```

# ---

# ## **The Trick**

# **Naive approach:** Square everything, then sort → O(n log n)

# **Better approach:** Use two pointers! → O(n)

# **Key insight:**
# - Array is already sorted
# - Largest squares come from **either end** (biggest negative or biggest positive)
# - Build result array **backwards** from largest to smallest

# ---

# ## **Strategy: Two Pointers**
# ```
# nums = [-4, -1, 0, 3, 10]
#         ↑              ↑
#       left           right

# Compare:
# left² = (-4)² = 16
# right² = (10)² = 100

# 100 > 16, so put 100 at the END of result
# Move right pointer left

# Result: [?, ?, ?, ?, 100]
# ```

# **Visual:**
# ```
# Step 1: [-4, -1, 0, 3, 10]
#          ↑              ↑
#          16 vs 100 → Take 100
#          Result: [_, _, _, _, 100]

# Step 2: [-4, -1, 0, 3]
#          ↑           ↑
#          16 vs 9 → Take 16
#          Result: [_, _, _, 16, 100]

# Step 3: [-1, 0, 3]
#          ↑     ↑
#          1 vs 9 → Take 9
#          Result: [_, _, 9, 16, 100]

# Step 4: [-1, 0]
#          ↑  ↑
#          1 vs 0 → Take 1
#          Result: [_, 1, 9, 16, 100]

# Step 5: [0]
#          Take 0
#          Result: [0, 1, 9, 16, 100] ✅