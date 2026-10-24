class Solution:

    def encode(self, strs: List[str]) -> str:
        # length#str
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        # joins everything in array
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # look for start of string + length
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # start of string
            i = j + 1
            res.append(s[i:i + length])
            i = i + length
        return res

