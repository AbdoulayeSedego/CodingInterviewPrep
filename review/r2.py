from typing import List
#problem 2
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Code from scratch - Kadane's algorithm
        current_sum = nums[0] #set to first ele
        max_sum = nums[0] #set to first ele
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i]) #compare curent ele to sum of current ele
            max_sum = max(max_sum, current_sum) #compare current sum to max_sum
        return max_sum

# Test
solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6