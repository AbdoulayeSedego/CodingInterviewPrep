from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        result = []
        for i, j in nums.most_common(k):
            result.append(i)
        return result

            

# Test
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
print(solution.topKFrequent([1], 1))  # [1]