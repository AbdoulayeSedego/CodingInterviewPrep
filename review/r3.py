class Solution:
    #problem 3
    def isValid(self, s: str) -> bool:
        # Code from scratch - stack approach
        stack = []
        match_char = {')':'(',']':'[','}':'{'}
        
        for c in s:
            if c in match_char:
                if not stack or stack[-1] != match_char[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
                
        return len(stack) == 0

# Test
solution = Solution()
print(solution.isValid("()[]{}"))  # True
print(solution.isValid("([)]"))    # False