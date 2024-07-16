class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        st = set()
        for num in nums: 
            if num in st:
                return True
            else: 
                st.add(num)
        return False

if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().containsDuplicate(nums)) # True

    nums = [1, 2, 3, 4]
    print(Solution().containsDuplicate(nums)) # False

    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(Solution().containsDuplicate(nums)) # True