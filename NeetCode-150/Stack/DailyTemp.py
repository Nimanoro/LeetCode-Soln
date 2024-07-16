class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        res = [0 for _ in temperatures]
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append(i)
            while stack and temperatures[stack[-1]] < temp:
                res[stack[-1]] = (i - stack[-1])
                stack.pop()
            stack.append(i)
        return res
    
if __name__ == "__main__":
    temp = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(temp)) # [1, 1, 4, 2, 1, 1, 0, 0]s

    temp = [30, 40, 50, 60]
    print(Solution().dailyTemperatures(temp)) # [1, 1, 1, 0]