from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Your code here
        result = []
        
        nums = Counter(nums)
        #return the most frequent element in the dict
        for i, j in nums.most_common(k):
                result.append(i)
        return result
        

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.topKFrequent([1,1,1,2,2,3], 2))  # Expected: [1,2]
    print(solution.topKFrequent([1], 1))  # Expected: [1]