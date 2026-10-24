class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)
        ans_ind = 0
        for _ in range(2):
            for i in range(0, len(nums)):
                ans[ans_ind] = nums[i]
                ans_ind += 1
        return ans