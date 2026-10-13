class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # input: piles of bananas (array of int), number of hours to finish all (int)
        # output: minimum bananas to eat within h hours
        # goal: find the minimum number of bananas you can eat within h hours
        # constraints: cannot eat more than 1 pile

        # [1,4,3,2], 9: 2
        # can h be less than the number of piles?: no

        # initial approach:
        # iterate from 1 to max of arr
            # iterate through each index of the array
                # add ceil(val / index) to hour count
            # min of hour count
        
        # optimize approach:
        # binary search on search range [1, max val in array]
        l, r = 1, max(piles)
        min_count = max(piles)
        while l <= r:
            m = (l + r) // 2
            hour_count = 0
            # iterate through each index of array
            for val in piles:
                hour_count += math.ceil(val / m)
                # add ceil(val / index) to hour count
            if hour_count <= h:
                r = m - 1
            else:
                # minimum will always be on left
                l = m + 1

            # if min < min_count and hour count <= 9, set min
            # if min is greater, move right right
            # if hour count > 9, move left left
        return l