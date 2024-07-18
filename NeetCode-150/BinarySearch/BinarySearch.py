class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if (nums[mid] == target):
                return mid
            elif (nums[mid]> target):
                right = mid - 1
            else: 
                left = mid + 1
        return -1
    
if __name__ == "__main__":
    s = [-1,0,3,5,9,12]
    print(Solution().search(s, 9)) # 4

    t = [-1,0,3,5,9,12]
    print(Solution().search(t, 2)) # -1

    u = [-1,0,3,5,9,12]
    print(Solution().search(u, 13)) # -1