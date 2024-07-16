class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        ops = {"+": "plus", "*" : "mul", "/": "div", "-": "sub"}
        for char in tokens:
            if char in ops:
                num1 = stack.pop()
                num2 = stack.pop()
                if ops[char] == "plus":
                    stack.append(num1 + num2)
                elif ops[char] == "mul":
                    stack.append(num1 * num2)
                elif ops[char] == "div":
                    stack.append(int(num2 /num1))
                elif ops[char] == "sub":
                    stack.append(num2 - num1)
            else: 
                stack.append(int(char))
        return stack[-1]
    
if __name__ == "__main__":
    tokens = ["2", "1", "+", "3", "*"]
    print(Solution().evalRPN(tokens)) # 9

    tokens = ["4", "13", "5", "/", "+"]
    print(Solution().evalRPN(tokens)) # 6