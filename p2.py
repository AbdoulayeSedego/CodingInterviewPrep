from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Your code here
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        return s == t

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.isAnagram("anagram", "nagaram"))  # Expected: True
    print(solution.isAnagram("rat", "car"))  # Expected: False