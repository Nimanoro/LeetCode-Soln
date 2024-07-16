import unittest
class Solution:
    def topKFrequent(self, nums , k):
        tots = {}
        freq = [[] for num in nums]
        for num in nums:
            tots[num] = tots.get(num, 0) + 1
        for num, rep in tots.items():
            freq[rep - 1].append(num)
        res = []
        for i in reversed(range(0, len(nums))):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_top_k_frequent_basic(self):
        input_data = [1, 1, 1, 2, 2, 3]
        k = 2
        expected_output = [1, 2]  # This is intentionally incorrect to see if the test catches it
        output = self.solution.topKFrequent(input_data, k)
        print(f"Expected: {expected_output}, Got: {output}")
        self.assertEqual(sorted(output), sorted(expected_output))

    def test_top_k_frequent_large_input(self):
        input_data = [1]*1000 + [2]*5000 + [3]*2000 + [4]*5000
        k = 2
        expected_output = [2, 4]  
        output = self.solution.topKFrequent(input_data, k)
        print(f"Expected: {expected_output}, Got: {output}")
        self.assertEqual(sorted(output), sorted(expected_output))

if __name__ == "__main__":
    unittest.main()
