from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Your code here
        current_sum = nums[0]
        max_sum     = nums[0]
        for i in range(1,len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(current_sum, max_sum)
            
        return max_sum


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected: 6
    print(solution.maxSubArray([1]))  # Expected: 1
    print(solution.maxSubArray([5,4,-1,7,8]))  # Expected: 23