from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n -1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        return result 


# Test
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))  # [24,12,8,6]
# Explanation: [2*3*4, 1*3*4, 1*2*4, 1*2*3]

print(solution.productExceptSelf([-1,1,0,-3,3]))  # [0,0,9,0,0]