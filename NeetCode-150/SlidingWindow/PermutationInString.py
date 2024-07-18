class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26
        for i in range(0, len(s1)):
            arr1[ord(s1[i]) - ord("a")] += 1
        l = 0 
        r = 0
        while r < len(s2):
            arr2[ord(s2[r]) - ord("a")] += 1
            if arr2 == arr1:
                return True
            if r - l == len(s1) - 1:
                arr2[ord(s2[l]) - ord("a")] -= 1
                l += 1
                r += 1
                continue
            r = r + 1
        return False
if __name__ == "__main__":
    s = Solution()
    print(s.checkInclusion("ab", "eidbaooo")) #True
    print(s.checkInclusion("ab", "eidboaoo")) #False
    print(s.checkInclusion("adc", "dcda")) #True
    print(s.checkInclusion("hello", "ooolleoooleh")) #False