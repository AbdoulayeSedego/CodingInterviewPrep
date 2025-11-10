from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i
        return 

 


# Test
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))  # [0,1]
print(solution.twoSum([3,2,4], 6))      # [1,2]