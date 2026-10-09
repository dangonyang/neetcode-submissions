class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        
        for i in range(n + 1):
            count = 0
            num = i
            while num:
                if num % 2 == 1:
                    count += 1
                num = num >> 1
            res.append(count)
        return res