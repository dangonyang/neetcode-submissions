class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        edge_roman = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}

        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and s[i] in edge_roman and s[i + 1] in edge_roman[s[i]]:
                total -= roman_int[s[i]]
            else:
                total += roman_int[s[i]]

        return total