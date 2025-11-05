from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Your code here
        unique = set()
        for i in range(len(nums)):
            if nums[i] in unique:
                return True
            unique.add(nums[i]) 
        return False

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test 1
    print(solution.containsDuplicate([1,2,3,1]))  # Expected: True
    
    # Test 2
    print(solution.containsDuplicate([1,2,3,4]))  # Expected: False
    
    # Test 3
    print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # Expected: True