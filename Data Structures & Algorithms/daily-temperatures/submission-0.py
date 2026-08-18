class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] # (temp, index)

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTempPair = stack.pop()
                output[stackTempPair[1]] = i - stackTempPair[1]
            stack.append((t,i))
        return output