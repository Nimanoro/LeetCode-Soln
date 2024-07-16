class Solution:
    def maxArea(self, height) -> int:
        left = 0
        right = len(height) - 1
        mx = 0 
        while left < right:
            mx = max(min(height[left], height[right]) * (right - left), mx) 
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return mx

        
if __name__ == "__main__":
    s = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(s)) # 49

    t = [1,1]
    print(Solution().maxArea(t)) # 1

    u = [4,3,2,1,4]
    print(Solution().maxArea(u)) # 16