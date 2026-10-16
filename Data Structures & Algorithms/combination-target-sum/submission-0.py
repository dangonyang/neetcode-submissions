class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            # go through tree decision that adds num
            dfs(i, cur, total + nums[i])
            cur.pop()
            # go through tree decision that doesn't add num
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res
