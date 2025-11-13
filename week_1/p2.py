from typing import List
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Your code here
        # # split and sort the string
        # s = ''.join(sorted(s))
        # t = ''.join(sorted(t))

        return Counter(s) == Counter(t)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.isAnagram("anagram", "nagaram"))  # Expected: True
    print(solution.isAnagram("rat", "car"))  # Expected: False