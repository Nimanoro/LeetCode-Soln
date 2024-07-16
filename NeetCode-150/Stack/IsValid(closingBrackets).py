class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for char in s:
            if char in dic and stack:
                if dic[char] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            if char in dic and not stack:
                return False
            else:
                stack.append(char)
        if stack:
            return False
        return True
    

if __name__ == "__main__":
    s = "()"
    print(Solution().isValid(s)) # True

    t = "()[]{}"
    print(Solution().isValid(t)) # True

    v = "(]"
    print(Solution().isValid(v)) # False

    w = "([)]"
    print(Solution().isValid(w)) # False

    x = "{[]}"
    print(Solution().isValid(x)) # True