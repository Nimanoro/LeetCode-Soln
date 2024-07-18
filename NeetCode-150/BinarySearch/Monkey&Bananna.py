from math import ceil
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        
        def homany(spd):
            t = 0 
            for num in piles:
                t += ceil(num / spd)
            return t
        
        mx = max(piles)
        if h == len(piles):
            return mx
        
        left = 1
        right = mx
        while left < right:
            mid = left + (right - left) // 2
            if homany(mid) <= h:
                right = mid 
            else:
                left = mid + 1 
        
        return left  
    
if __name__ == "__main__":
    s = [3,6,7,11]
    h = 8
    print(Solution().minEatingSpeed(s, h)) # 4

    t = [30,11,23,4,20]
    h = 5
    print(Solution().minEatingSpeed(t, h)) # 30

    u = [30,11,23,4,20]
    h = 6
    print(Solution().minEatingSpeed(u, h)) # 23