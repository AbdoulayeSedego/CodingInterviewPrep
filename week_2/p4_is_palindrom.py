class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        s = s.lower()
        for i in s:
            if i.isalnum():
                result.append(i)
        result = ''.join(result)
        
        return result == result[::-1]
        

# Test
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True
print(solution.isPalindrome("race a car"))  # False
print(solution.isPalindrome(" "))  # True
# ```

# **Problem:** Check if a string is a palindrome (reads same forwards and backwards).

# **Rules:**
# - Only consider **alphanumeric characters** (letters and numbers)
# - Ignore spaces, punctuation, capitalization

# **Examples:**
# ```
# "A man, a plan, a canal: Panama"
# → Clean: "amanaplanacanalpanama"
# → Palindrome? YES ✅

# "race a car"
# → Clean: "raceacar"
# → Palindrome? NO ❌