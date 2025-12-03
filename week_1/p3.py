from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Your code here
        if not strs: 
            return [[""]]
        result = defaultdict(list)
        for i in strs:
            signature = ''.join(sorted(i))
            result[signature].append(i)
        return list(result.values())



# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # Expected: [["bat"],["nat","tan"],["ate","eat","tea"]] (any order)
    
    print(solution.groupAnagrams([""]))
    # Expected: [[""]]