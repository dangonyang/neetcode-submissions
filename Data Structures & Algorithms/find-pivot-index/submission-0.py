class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        preSum = 0

        for i in range(len(nums)):
            if total - preSum - nums[i] == preSum:
                return i
            preSum += nums[i]
            # 11
        return -1
