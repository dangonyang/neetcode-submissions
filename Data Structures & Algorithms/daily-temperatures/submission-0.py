class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [temp, index]
        stk = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # iterate until find bigger temperature, then stop subtracting
            while stk and t > stk[-1][0]:
                stkT, stkI = stk.pop()
                res[stkI] = i - stkI
            stk.append((t, i))
        return res