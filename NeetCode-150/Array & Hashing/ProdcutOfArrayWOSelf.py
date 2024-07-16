class Solution:
      def productExceptSelf(self, nums):
        prefix = [1 for _ in nums]
        postfix = [1 for _ in nums]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in reversed(range(0, len(nums) - 1)):
            postfix[i] = postfix[i+1] * nums[i+1]
        
        for i in range(0, len(nums)):
            prefix[i] = (prefix[i] * postfix[i])
        return prefix

if __name__ == "__main__":
    s = [1, 2, 3, 4]
    print(Solution().productExceptSelf(s)) # [24, 12, 8, 6]

    t =  [1, 2, 3, 4, 5]
    print(Solution().productExceptSelf(t)) # [120, 60, 40, 30, 24]