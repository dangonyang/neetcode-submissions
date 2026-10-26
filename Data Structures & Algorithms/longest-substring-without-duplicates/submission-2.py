class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        l = 0
        length = 0

        for r in range(len(s)):
            while s[r] in window and window[s[r]] > 0:
                window[s[l]] -= 1
                l += 1
            window[s[r]] += 1
            length = max(length, r - l + 1)
        return length