class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum= sum(nums)
        leftsum= 0
        for i in range(len(nums)):
            if (totalsum-leftsum-nums[i])==leftsum:
                return i
            leftsum+=nums[i]
        return -1
