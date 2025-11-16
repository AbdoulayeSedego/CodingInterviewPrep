class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set()
        max_length = 0

        for right in range(len(s)):
            #while duplicate exists, remove them to shrink the window
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            #add current character
            char_set.add(s[right])
            #update max lenght
            max_length = max(max_length, right - left + 1)
        return max_length


# Test
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))  # 3 ("abc")
print(solution.lengthOfLongestSubstring("bbbbb"))     # 1 ("b")
print(solution.lengthOfLongestSubstring("pwwkew"))    # 3 ("wke")
print(solution.lengthOfLongestSubstring(""))          # 0
# ```

# **Problem:** Find length of longest substring without repeating characters.

# **Examples:**
# ```
# "abcabcbb" → "abc" has length 3
# "bbbbb" → "b" has length 1
# "pwwkew" → "wke" has length 3
# ```

# ---

# ## **Strategy: Sliding Window + Hash Set**

# **The idea:**
# 1. Use a **window** (left and right pointers)
# 2. Expand window by moving right
# 3. If character repeats, shrink from left
# 4. Track maximum window size

# **Visual:**
# ```
# "abcabcbb"
#  ↑ left
#  ↑ right
# window = {a}, length = 1

# "abcabcbb"
#  ↑   ↑
# window = {a,b}, length = 2

# "abcabcbb"
#  ↑     ↑
# window = {a,b,c}, length = 3

# "abcabcbb"
#  ↑       ↑
# 'a' is duplicate! Shrink from left
# window = {b,c}, then add 'a'
# window = {b,c,a}, length = 3