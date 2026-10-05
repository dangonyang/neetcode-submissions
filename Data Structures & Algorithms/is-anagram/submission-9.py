class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = Counter(s)
        for ch in t:
            if ch not in count_s:
                return False
            count_s[ch] -= 1
            if count_s[ch] == 0:
                del count_s[ch]
        return True