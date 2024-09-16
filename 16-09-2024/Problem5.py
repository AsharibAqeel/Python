from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1         
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k
sol = Solution()
nums = [1, 1, 2, 2, 3, 4, 4]
k = sol.removeDuplicates(nums)
print(f"Number of unique elements: {k}")
print(f"Array after removing duplicates: {nums[:k]}")
