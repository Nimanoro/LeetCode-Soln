from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if not nums:
            return []
        if k == 1:
            return nums
        l = 0 
        r = 0
        res = []
        deq = deque()
        for r in range(len(nums)):
            while deq and nums[deq[-1]] < nums[r]:
                deq.pop()
            deq.append(r)
            while deq and l > deq[0] :
                deq.popleft()
            if r - l + 1 == k:
                res.append(nums[deq[0]])
                l += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) #[3,3,5,5,6,7]
    print(s.maxSlidingWindow([1], 1)) #[1]
    print(s.maxSlidingWindow([1,-1, 4], 2)) #[1,4]