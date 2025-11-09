from collections import Counter
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Your code here
        # container = []
        # st = s.lower()
        # st = ''.join(st)
        # for i in st:
        #     if i.isalnum() or i.isalpha():
        #         container.append(i)
        # st = ''.join(container)
        # return st == st[::-1]

        result = ''.join(p.lower() for p in s if p.isalnum())
        return result == result[::-1]


# Test
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(solution.isPalindrome("race a car"))  # False