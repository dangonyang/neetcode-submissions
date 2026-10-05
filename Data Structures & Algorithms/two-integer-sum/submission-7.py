class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        
        for i, num in enumerate(nums):
            hit = target - num
            if hit in hm:
                return [hm[hit], i]
            hm[num] = i
        return []  