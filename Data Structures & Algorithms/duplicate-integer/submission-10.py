class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visit = {}

        for i, num in enumerate(nums):
            if num in visit:
                return True
            visit[num] = i
        return False