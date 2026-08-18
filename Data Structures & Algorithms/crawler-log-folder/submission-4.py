class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in range(len(logs)):
            if len(stack) > 0 and logs[i] == "../":
                stack.pop()
            elif logs[i] == './':
                continue    
            elif logs[i] != "../":
                stack.append(logs[i])
            
        return len(stack)
            