class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # is it possible to have all vals in nums to be equal to val? -> yes, return 0
        # can nums be empty? yes -> return 0

        # [1, 1], val = 1 -> 0
        # [3,2,2,3], val = 3 -> 2
        # [0,1,2,2,3], val = 2 -> 3

        # goal: first k elements of nums is not equal to val and return k
        # initial approach: O(n^2) (t) O(1) (s)
        # iterate through each value in nums
        #   if curr is equal to val
        #       iterate starting curr index + 1 
        #           if this index != val, swap with curr index and add to count
        #   else add to count

        # optimize initial (two pointer):
        # left = start (keeps track of val that needs to be swapped)
        # iterate through each value in nums, where right is tracking:
        #   if curr val != val, 
        #       if left == val 
        #           swap left and right 
        #           add one to left
        #       add to k
        #   if curr val == k, left = right

        left = 0
        k = 0
        for right in range(len(nums)):
            if nums[right] != val:
                if nums[left] == val:
                    temp = nums[right]
                    nums[right] = nums[left]
                    nums[left] = temp
                    left += 1
                k += 1
            else:
                if nums[left] != val:
                    left = right
        return k

        # left = 2
        # right = 3
        # k = 2