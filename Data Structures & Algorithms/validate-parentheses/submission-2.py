class Solution:
    def isValid(self, s: str) -> bool:
        hm = {'(': ')', '{': '}', '[': ']'}
        stk = []

        for c in s:
            if c in hm:
                stk.append(hm[c])
            elif c in hm.values() and stk:
                compare = stk.pop()
                if compare != c:
                    return False
            else:
                return False
        return not stk
                