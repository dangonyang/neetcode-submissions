class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # pretend i asked clarifying questions

        # input: nums (integer array), lower bound sum (int), upper bound sum (int)
        # output: number of qualifying pairs that sum into the bounds
        # goal: find the number of pairs

        # initial approach:
        # iterate through the entire array
            # iterate through the rest of the array after the current element of the outside array
                # see if outside and inside within bounds, increase their count
        
        # [-3, 1, 2, 5]
        # []
        # optimize initial:
        # sort the array
        # helper function that takes in value that's the limit
            # left starts at start of array, right starts at end 
            # while left < right
                # if current total less than limit
                    # add total of all pairs between left and right are valid
        nums.sort()
        def at_most(limit):
            left, right, total = 0, len(nums) - 1, 0
            while left < right:
                if nums[left] + nums[right] <= limit:
                    total += right - left
                    left += 1
                else:
                    right -= 1
            return total
        return at_most(upper) - at_most(lower - 1)
        
