class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = abs(x)
        
        array = []
        while x:
            array.append(x % 10)
            x = x // 10

        # [4, 3, 2, 1]
        # length = 4
        # (10 ** (length - 1)) * index
        length = len(array) 
        res = 0
        for i in range(len(array)):
            res += (10 ** (length - 1)) * array[i]
            length -= 1
        
        if negative:
            res *= -1
        if (res > (2 ** 31) - 1) or (res < -2 ** 31):
            return 0
        return res
            