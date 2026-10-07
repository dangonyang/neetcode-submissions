class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        operators = ['+', '-', '*', '/']
        num_stk = []
        operation = 0

        for token in tokens:
            if token not in operators:
                num_stk.append(token)
            else:
                second = int(num_stk.pop())
                first = int(num_stk.pop())
                if token == '+':
                    operation = first + second
                elif token == '-':
                    operation = first - second
                elif token == '*':
                    operation = first * second
                elif token == '/':
                    operation = int(first / second)

                num_stk.append(operation)
        return operation