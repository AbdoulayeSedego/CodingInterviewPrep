from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return[1+left, 1+right]
            elif current_sum < target:
                left +=1
            else:
                right -=1
        return []

# Test
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))  # [1,2] (1-indexed!)
print(solution.twoSum([2,3,4], 6))      # [1,3]
print(solution.twoSum([-1,0], -1))      # [1,2]