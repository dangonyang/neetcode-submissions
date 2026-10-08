class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        if len(t) > len(s):
            return ""
        
        res = ""
        left = 0
        letter_count_t = Counter(t)
        window = Counter()
        match_count = 0

        # moves right pointer
        for right in range(len(s)):
            # checks letter frequency per window
            curr_s = s[left:right + 1]

            # if ending letter in window is in t
            if s[right] in letter_count_t:
                window[s[right]] += 1

                # if letter frequency of ending letter matches t's
                if window[s[right]] == letter_count_t[s[right]]:
                    # add 1 to represent number of unique letters in window that matches requirement
                    match_count += 1

                    # checks to see if unique char match freq -> means window is valid
                    if match_count == len(letter_count_t):
                        # replace if curr string is shorter
                        if res == "" or len(res) > len(curr_s):
                            res = curr_s

            # shrink while window is valid
            while match_count == len(letter_count_t):
                if res == "" or (right - left + 1) < len(res):
                    res = s[left:right + 1]
                
                # if first char of window is in t
                if s[left] in letter_count_t:
                    # remove 1 frequency of first char of window
                    window[s[left]] -= 1
                    # if letter frequency of window doesn't match
                    if window[s[left]] < letter_count_t[s[left]]:
                        # remove 1 count of matching char
                        match_count -= 1
                # move pointer
                left += 1

        return res
