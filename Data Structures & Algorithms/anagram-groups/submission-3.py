class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                # count array indicating how many letters are in each word
                count[ord(c) - ord('a')] += 1
            # key = anagram array, append string to list
            res[tuple(count)].append(s)
        return list(res.values())
        