class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        # represents empty prefix (base case)
        prefixSum = { 0 : 1 }

        for n in nums:
            curSum += n
            # can remove a prefix sum of diff, there can be +1
            diff = curSum - k

            # counts subarrays ending here with sum k
            res += prefixSum.get(diff, 0)
            # increment number of prefix sums that this pre. sum
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return res