class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set for O(1) lookups
        hm = set(nums)
        longest = 0
        for num in hm:
            # start of new sequence
            if (num - 1) not in hm:
                length = 1
                # keep finding +1
                while (num + length) in hm:
                    length += 1
                longest = max(length, longest)
        return longest