class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1
        
        return False