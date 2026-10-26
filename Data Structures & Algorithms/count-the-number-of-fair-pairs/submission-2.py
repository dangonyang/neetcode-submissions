class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def at_most(limit):
            total = 0
            l, r = 0 , len(nums) - 1
            while l < r:
                if nums[l] + nums[r] <= limit:
                    total += r - l
                    l += 1
                else:
                    r -= 1
            return total
        return at_most(upper) - at_most(lower - 1)
