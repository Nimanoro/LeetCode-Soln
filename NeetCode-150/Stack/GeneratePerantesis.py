class Solution:
    def generateParenthesis(self, n: int):
        stack = []
        res = []
        def backtrack(openn, closen):
            if openn == n and closen == n:
                res.append("".join(stack))
                return 
            if openn < n:
                stack.append("(")
                backtrack(openn+1, closen)
                stack.pop()
            if closen < n and closen < openn:
                stack.append(")")
                backtrack(openn, closen + 1)
                stack.pop()
        backtrack(0,0)
        return res
        
if __name__ == "__main__":
    s = 3
    print(Solution().generateParenthesis(s)) # ["((()))","(()())","(())()","()(())","()()()"]