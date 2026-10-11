class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = ""
        if s == "":
            return 0

        # sliding window: left and right
        # hash map to record characters and their last seen index
        left = 0
        seen = {}
        length = 1
        # s = "zxyz"
        # left = 1
        # seen = {"z": 3, "x": 1, "y": 2}
        # right = 3
        # length = 3
        for right, ch in enumerate(s):
            # if ch in seen and it's in the window
            if ch in seen and left <= seen[ch]:
                # until we update new character's last seen index
                while seen[ch] != right:
                    if s[left] == ch:
                        seen[ch] = right
                    left += 1
            length = max(length, right - left + 1)
            seen[ch] = right
        return length

