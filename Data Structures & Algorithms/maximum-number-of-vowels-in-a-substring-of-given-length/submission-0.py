class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count, answer = 0, 0
        for i, c in enumerate(s):
            count += c in "aeiou"
            if i >= k:
                count -= s[i-k] in "aeiou"
            if i >= k - 1:
                answer = max(answer, count)
        return answer

