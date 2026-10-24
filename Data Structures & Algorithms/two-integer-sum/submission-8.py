class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       visit = {}

       for i, num in enumerate(nums):
            hit = target - num
            if hit in visit:
                return [visit[hit], i]
            visit[num] = i