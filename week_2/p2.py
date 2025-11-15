from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Creates empty dictionary
        result = defaultdict(list)
        #return empty list if strs is empty
        if not strs:
            return [[""]]
        for i in strs:
            #Creates a unique identifier for anagrams
            signature = ''.join(sorted(i))
            #Adds the original word to its signature's group, group them
            result[signature].append(i)
            #Extracts just the groups (values), ignoring signatures (keys) and return values
        return list(result.values())

# Test
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# [["bat"],["nat","tan"],["ate","eat","tea"]]