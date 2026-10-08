class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if (x // 10) < 1:
            return True
        
        # array approach
        # e.g. 1221
        # 1221 % 10 gives us the last digit -> put into array
        # 1221 // 10 update num

        # 1221 % 10 = 1
        # 11 % 10 = 1
        # 1 
        
        num_array = []
        while x:
            num_array.append(x % 10)
            x = x // 10

        l = 0
        r = len(num_array) - 1
        while l < r:
            if num_array[l] != num_array[r]:
                return False
            l += 1
            r -= 1
        return True
