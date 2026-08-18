class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+', '-', '*', '/']
        res = deque()
        for i in range(len(tokens)):
            if tokens[i] not in operations:
                res.append(tokens[i])
            else:
                b = int(res.pop())
                a = int(res.pop())
                res.append(self.operate(operations,tokens[i], a, b))
        return int(res[-1])
    
    def operate(self, operations ,operation: str, a, b):
        if operation == operations[0]:
            return a + b
        elif operation == operations[1]:
            return a - b
        elif operation == operations[2]:
            return a * b
        else:
            return a / b