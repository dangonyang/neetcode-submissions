class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # [1, 2, 1]
        # [1, 2, 1, 0, 4, 2, 6]
        output  = []
        q = collections.deque() # contain index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output

        