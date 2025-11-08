class Solution:
    def isValid(self, s: str) -> bool:
        # Your code here
        stack = []
        # Dictionary to match closing to opening brackets
        matching = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in matching:
                # Check if it matches the most recent opening
                if not stack or stack[-1] != matching[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0 # return empty if all bracket matched 




# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.isValid("()"))      # Expected: True
    print(solution.isValid("()[]{}"))  # Expected: True
    print(solution.isValid("(]"))      # Expected: False
    print(solution.isValid("([)]"))    # Expected: False
    print(solution.isValid("([])"))    # Expected: True