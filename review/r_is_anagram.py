from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ###Solution 1
        # s = ''.join(sorted(s))
        # t = ''.join(sorted(t))
        # return s == t

        ###Solution 2
        return Counter(s) == Counter(t)

# Test
solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))  # True
print(solution.isAnagram("rat", "car"))  # False