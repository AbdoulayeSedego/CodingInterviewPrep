from typing import List
#from collections import Counter

class Solution:
    #problem 1
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Code from scratch - hash map approach
        seen = {} #dict
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i
           
            




# Test
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))  # [0,1]

# stp 1:
# c = 9 - 2 = 7
#stp 2:
# c = 9 - 7 = 2