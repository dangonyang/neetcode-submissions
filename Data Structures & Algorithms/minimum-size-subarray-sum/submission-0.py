class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_pointer, total = 0, 0
        res = float("inf")
        
        for right_pointer in range(len(nums)):
            total += nums[right_pointer]
            while total >= target:
                res = min(right_pointer - left_pointer + 1, res)
                total -= nums[left_pointer]
                left_pointer += 1
        return 0 if res == float("inf") else res
