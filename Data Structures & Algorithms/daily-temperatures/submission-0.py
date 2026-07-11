class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for currindex, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                previndex, num = stack.pop()
                res[previndex] = currindex - previndex
            stack.append((currindex, temp))
        return res
        