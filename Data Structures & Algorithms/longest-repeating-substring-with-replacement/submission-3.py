class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        length = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            window[s[r]] += 1
            max_freq = max(max_freq, window[s[r]])
            while l < r and (r - l + 1 - max_freq) > k:
                window[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
        return length