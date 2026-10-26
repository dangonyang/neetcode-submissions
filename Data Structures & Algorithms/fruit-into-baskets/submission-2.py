class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window
        # check length of sliding window
        # increase left pointer if we encounter a fruit outside of our 

        # [1, 2, 1, 2, 2, 3, 3, 3, 3]
        l = 0
        fruits1 = fruits[0]
        fruits2 = -1
        fruits1_lastInd = 0
        fruits2_lastInd = -1
        total = 1

        for r in range(len(fruits)):
            f = fruits[r]
            if f == fruits1:
                fruits1_lastInd = r
            elif f == fruits2 or fruits2 == -1:
                fruits2_lastInd = r
                fruits2 = f
            else:
                # fruit with smaller index gets replaced
                if fruits2_lastInd == min(fruits1_lastInd, fruits2_lastInd):
                    fruits1_lastInd, fruits2_lastInd = fruits2_lastInd, fruits1_lastInd
                    fruits1, fruits2 = fruits2, fruits1
                
                l = fruits1_lastInd + 1
                fruits1 = f
                fruits1_lastInd = r
            total = max(total, r - l + 1)
        return total
            