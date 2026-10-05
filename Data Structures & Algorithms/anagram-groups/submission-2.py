class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = collections.defaultdict(list)

        for word in strs:
            key = str(sorted(list(word)))
            seen[key].append(word)
        return list(seen.values())