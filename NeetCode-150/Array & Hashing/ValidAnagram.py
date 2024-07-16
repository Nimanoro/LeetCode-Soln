class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for char in s:
            dic[char] = dic.get(char, 0) + 1
        for char in t:
            if char not in dic:
                return False
            else: 
                dic[char] -= 1
        b = 0
        for key, val in dic.items():
            if val != 0:
                b = 1
        if b == 1:
            return False
        return True
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t)) # True

    s = "rat"
    t = "car"
    print(Solution().isAnagram(s, t)) # False