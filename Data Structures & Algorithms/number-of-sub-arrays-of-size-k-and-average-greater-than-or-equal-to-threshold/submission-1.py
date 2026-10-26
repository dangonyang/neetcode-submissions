class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        l = 0
        curTotal = 0

        for r in range(len(arr)):
            if r - l + 1 > k:
                curTotal -= arr[l]
                l += 1
            curTotal += arr[r]
            if r - l + 1 == k and (curTotal / k) >= threshold:
                res += 1
        return res
        