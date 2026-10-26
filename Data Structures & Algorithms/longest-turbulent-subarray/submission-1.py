class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # even indices must be bigger than the odd ones
        # or vice versa
        # basically just check if next index is greater than
        # sliding window (variable size)
        l = 0
        less = True
        greater = True
        length = 0
        # iterate through each element starting from 1 and end len - 2
        for r in range(len(arr) - 1):
            # two cases:
            # arr[r] > arr[r + 1]
            # arr[r] < arr[r + 1]
            if arr[r] < arr[r + 1] and less:
                # increment r
                less = False
                greater = True          
            elif arr[r] > arr[r + 1] and greater:
                greater = False
                less = True
            elif arr[r] == arr[r + 1]:
                l = r + 1
                less = True
                greater = True
            else:
                l = r
                # save last sign if this is a valid window
                if arr[r] < arr[r + 1]:
                    less = False
                    greater = True 
                else:
                    less = True
                    greater = False
            length = max(length, r - l + 1)
        return length + 1