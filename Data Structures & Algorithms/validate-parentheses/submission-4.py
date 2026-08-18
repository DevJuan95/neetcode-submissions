class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        closing_chars = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            if char in closing_chars:
                if stack and closing_chars[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        return True and len(stack) == 0
