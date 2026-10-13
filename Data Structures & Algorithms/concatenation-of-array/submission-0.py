class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # can nums be empty -> no
        # is nums all valid int -> yes

        # input: list of int
        # output: list of int (double the input)
        # goal: concatenate the input, so nums o nums

        # [1,4,1,2] -> [1,4,1,2,1,4,1,2]
        # [22,21] -> [22,21,22,21]
        # [1] -> [1,1] x

        # initial approach: 
        # create a dynamic array
        # iterate through nums twice, so outside loop is range of 2
            # iterate through each num in nums
                # append num to array
        # time: O(2n)=O(n), O(2n)=O(n)

        # optimize approach:
        # create an array double of input
        newArr = [0] * (len(nums) * 2)
        newInd = 0
        # iterate through nums twice
        for _ in range(1, 3):
            # iterate through each num in nums
            for i in range(len(nums)):
                # replace val at cur index with num
                newArr[newInd] = nums[i]
                newInd += 1
        return newArr
        # time: O(2n)=O(n)
        # space: O(1) (amortized time complexity)
            
