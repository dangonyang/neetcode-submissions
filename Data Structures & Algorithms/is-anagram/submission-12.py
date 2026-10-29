class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # are we guaranteed that the lengths of s and t are the same? no
        # do non-letters count? no

        # input: two strings (s and t)
        # output: true of false depending if anagram
        # goal: find out if the two given strings are an anagram

        # initial approach:
        # check if the lengths of s and t are equal
        # traverse through all characters in s
            # traverse through all characters in t
                # if s and t character equal, delete from both
        # see if s and t are ""

        # optimize:
        # lengths are equal?
        if len(s) != len(t):
            return False
        # have count_t and count_s be [0] * 26
        count_s = [0] * 26
        count_t = [0] * 26
        # traverse through each index in s
        for i in range(0, len(s)):
            # save number in count array by += 1
            count_s[ord(s[i]) - ord('a')] += 1
            count_t[ord(t[i]) - ord('a')] += 1
        # is count_s and count_t equal?
        return count_s == count_t
        

        
        