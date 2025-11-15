from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Modify nums in-place to move all 0's to the end 
        while maintaining relative order of non-zero elements.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1
        while left < len(nums):
            nums[left] = 0
            left += 1

        # left = 0  # Position for next non-zero
        
        # for right in range(len(nums)):
        #     if nums[right] != 0:
        #         # Swap non-zero with position at left
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1

            

# Test
solution = Solution()

nums1 = [0,1,0,3,12]
solution.moveZeroes(nums1)
print(nums1)  # [1,3,12,0,0]

nums2 = [0]
solution.moveZeroes(nums2)
print(nums2)  # [0]

nums3 = [0,0,1]
solution.moveZeroes(nums3)
print(nums3)  # [1,0,0]
# ```

# **Problem:** Move all zeros to the end, keep other numbers in order.

# **Constraints:**
# - Must modify array **in-place** (don't create new array)
# - Must maintain relative order of non-zero elements

# **Example:**
# ```
# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]