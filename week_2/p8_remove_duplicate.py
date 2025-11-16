from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # result = []
        # for i in nums:
        #     if i not in result:
        #         result.append(i)
        # return len(result)
        position = 1
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[position] = nums[i]
                position += 1
        return position

# Test
solution = Solution()

nums1 = [1,1,2]
k1 = solution.removeDuplicates(nums1)
print(k1, nums1[:k1])  # 2, [1, 2]

nums2 = [0,0,1,1,1,2,2,3,3,4]
k2 = solution.removeDuplicates(nums2)
print(k2, nums2[:k2])  # 5, [0, 1, 2, 3, 4]