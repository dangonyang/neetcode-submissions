class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 0 = 0
        # 1 = 1
        # 2 = 10
        # 3 = 11
        # 4 = 100
        n = len(nums)
        xorr = n
        for i in range(n):
            print(i ^ nums[i])
            xorr = xorr ^ (i ^ nums[i])
        return xorr
        