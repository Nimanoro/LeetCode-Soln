class Solution:
    def twoSum(self, numbers, target: int):
        left = 0
        right = len(numbers) - 1
        while left < right: 
            if target == numbers[left] + numbers[right]:
                return [left+ 1, right + 1]
            elif target > numbers[left] + numbers[right]:
                left += 1
            else:
                right -= 1
        return [-1]
        
if __name__ == "__main__":
    s = [2, 7, 11, 15]
    print(Solution().twoSum(s, 9)) # [1, 2]

    t =  [2, 3, 4]
    print(Solution().twoSum(t, 6)) # [1, 3]

    u = [5, 12 , 14, 15 , 25, 50 , 51, 52, 63 ,  75]
    print(Solution().twoSum(u, 100)) # [5,10]