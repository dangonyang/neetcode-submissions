class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # in case k > len(nums)
        k %= n 

        def reverse(l: int, r: int) -> None:
            while l < r:
                # swap
                nums[l], nums[r] = nums[r], nums[l] 
                l, r = l + 1, r - 1
        # reverse entire array
        reverse(0, n - 1)
        # reverse first k elements
        reverse(0, k - 1)
        # reverse rest of array back
        reverse(k, n - 1)