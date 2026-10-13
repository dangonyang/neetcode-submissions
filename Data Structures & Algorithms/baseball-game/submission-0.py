class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # can the input ever be empty? -> no
        # can we assume that all inputs will be valid? -> yes

        # input: list of strings
        # output: int
        # goal: take a list of strings and output the score based on the operations given

        # initial approach: 
        # iterate through operations
            # add numbers we see onto a list
            # iterate until non-number found
                # record it if found
            # do operation
        
        # optimize approach:
        op = {"D", "+", "C"}
        # create a stack
        stack = []
        # iterate through each val in operations
        for val in operations:
            # if number, we add to stack
            if val not in op:
                stack.append(val)
            # else, we do the operations
            else:
                if val == "D":
                    save = stack.pop()
                    double = int(save) * 2
                    stack.append(save)
                    stack.append(str(double))
                elif val == "+":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    num_sum = int(num1) + int(num2)
                    stack.append(str(num2))
                    stack.append(str(num1))
                    stack.append(str(num_sum))
                else:
                    stack.pop()
        res = 0
        for val in stack:
            res += int(val)
        return res