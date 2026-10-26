class Solution:
    def clearDigits(self, s: str) -> str:
        # input: string s
        # output: another string after we clear digits + associated letters
        # goal: find the new string based on the removal

        # initial approach:
        # one loop goes through letter
        # another loop goes through each number
        # remove along those loops

        # optimize approach:
        stk = []
        # for each character 
        for c in s:
            # if letter
            if 'a' <= c <= 'z':
                # append to stack
                stk.append(c)
            # if number
            elif '0' <= c <= '9':
                # pop from stack
                stk.pop()
        # return whatever is in the stack as a string
        return "".join(stk)