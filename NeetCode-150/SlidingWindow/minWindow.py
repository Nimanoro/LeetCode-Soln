class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count, window = {}, {}
        for char in t:
            count[char] = count.get(char, 0) + 1
        l = 0
        r = 0
        have, need = 0, len(count)
        reslen = float("inf")
        res1, res2 = 0,0 
        for r in range(len(s)):
            char = s[r]
            if char in count:
                window[char] = window.get(char, 0) + 1
                if window[char] == count[char]:
                    have += 1
            while have == need:
                if r - l < reslen:
                    res1, res2 = l, r
                    reslen = r - l
                char = s[l]
                if char in count:
                    if count[char] == window[char]:
                        break
                    else:
                        window[char] = window[char] - 1
                        l = l + 1
                else:
                    l = l + 1
        if reslen != float("inf"):
            return s[res1: res2 + 1] 
        else:
            return ""
                

if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC")) #BANC