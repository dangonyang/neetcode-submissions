class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # if current number is greater than 0, you cannot possibly have a sum to 0
            if nums[i] > 0:
                break
            # if we already visited this number skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # iterate through rest of list with two pointer
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    # too big
                    r -= 1
                elif threeSum < 0:
                    # too small
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # continue
                    l += 1
                    r -= 1

                    # if we already visited left pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
                