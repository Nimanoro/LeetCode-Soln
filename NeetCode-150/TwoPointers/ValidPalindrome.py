class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left = left + 1
                continue
            if not s[right].isalnum():
                right = right - 1
                continue
            if s[right].lower() != s[left].lower():
                return False
            if s[right].lower() == s[left].lower():
                right -= 1
                left += 1
                continue
        return True
    
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s)) # True

    t = "a B A"
    print(Solution().isPalindrome(t)) # True

    v = "AS!@#"
    print(Solution().isPalindrome(v)) # False