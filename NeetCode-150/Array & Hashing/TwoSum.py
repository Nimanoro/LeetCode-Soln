class Solution:
    def twoSum(self, nums, target: int):
        dic = {}
        for i, num in enumerate(nums):
            des = target - num
            if des in dic:
                return [dic[des], i]
            dic[num] = i 
    
if __name__ == "__main__":
    s = [2, 7, 11, 15]
    print(Solution().twoSum(s, 9)) # [0, 1]

    t =  [3, 2, 4]
    print(Solution().twoSum(t, 6)) #[1,2]