class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # can the array be empty? -> no
        # if the array is of length 1, do we return -1? -> yes

        # input: array of integers
        # output: array of integers
        # goal: replace every element in input with largest number of right (cannot make new array)
        
        # [3,3] -> [3,-1] x              
        # [1] -> [-1] x
        # [2,4,5] -> [5,5,-1] x

        # initial approach: 
        # iterate through each index
        #   iterate through rest of the array to find the maximum after
        #       if at end, max = -1
        #   update curr to max
        # time: O(n^2), space: O(1)

        # optimize approach:
        max_val = -1
        # iterate through nums, starting from the last index
        for i in range(len(arr) - 1, -1, -1):
        #   check if this is max value, if it is, save it with temp
            temp = arr[i] if arr[i] > max_val else max_val
        #   swap curr with max value
            arr[i] = max_val
        #   max is equal to temp
            max_val = temp
        return arr
        # time: O(n)
        # space: O(1)
