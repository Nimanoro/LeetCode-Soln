class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        st = set(nums)
        for num in st:
            temp = 1
            if num - 1 in st:
                continue
            if num + 1 in st:
                while num + 1 in st:
                    num = num + 1
                    temp = temp + 1
                    res = max(temp, res)
        return res
                    
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive(nums)) # 4

    nums = [0,3,7,2,5,8,4,6,0,1]
    print(Solution().longestConsecutive(nums)) # 9

    nums = [0,3,7,2,5,8,4,6,0,1,9,10,11,12]
    print(Solution().longestConsecutive(nums)) # 13