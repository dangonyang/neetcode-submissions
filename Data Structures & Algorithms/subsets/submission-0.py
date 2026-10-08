class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # input: list of int
        # output: list of int lists

        # goal: return all possible subsets of nums
        # method: backtracking

        res = []

        subset = []
        def dfs(i):
            # if past leaf node
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision to not include nums[i]
            subset.pop()
            dfs(i + 1)
            
        dfs(0)
        return res
                