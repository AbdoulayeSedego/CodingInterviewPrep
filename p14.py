from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Modify s in-place
        #reverse a string manually 
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        #solution 2
        #return s[:] = s[::-1] #modify original list

# Test
solution = Solution()
s = ["h","e","l","l","o"]
solution.reverseString(s)
print(s)  # ["o","l","l","e","h"]