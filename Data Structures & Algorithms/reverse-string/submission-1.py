class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # input: list of strings
        # output: list of strings through s

        # two pointer approach: 
        # left: beginning
        # right: end
        # for loop
        #   swap characters in left and right index
        
        # time complexity: O(n/2) -> O(n)
        # space complexity: O(1)
        print(len(s))

        left = 0
        for right in range(len(s) - 1, len(s) // 2 - 1, -1):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
        return s
        