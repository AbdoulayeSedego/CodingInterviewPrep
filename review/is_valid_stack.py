class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char = {')':'(', ']':'[', "}":'{'}

        for i in s:
            if i in char:
                if not stack or stack[-1] != char[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack) == 0
            

# Test
solution = Solution()
print(solution.isValid("()"))      # True
print(solution.isValid("()[]{}"))  # True
print(solution.isValid("(]"))      # False
print(solution.isValid("([)]"))    # False