class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stk = [] # pair of values [num, minLeft], mono decreasing
        curMin = nums[0]

        for n in nums[1:]:
            while stk and n >= stk[-1][0]:
                stk.pop()
            if stk and n > stk[-1][1]:
                return True
            stk.append([n, curMin])
            curMin = min(curMin, n)
        return False
