import unittest
class Solution:
    def groupAnagrams(self, strs):
        dic = {}
        for word in strs:
            srt = sorted(word)
            srt = "".join(srt)
            if srt in dic:
                dic[srt].append(word)
            else:
                dic[srt] = [word]
        res = []
        for k, v in dic.items():
            res.append(v)
        return res
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_group_anagrams_basic(self):
        input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected_output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        output = self.solution.groupAnagrams(input_data)
        output = [sorted(group) for group in output]
        expected_output = [sorted(group) for group in expected_output]
        self.assertEqual(sorted(output), sorted(expected_output))

    def test_group_anagrams_with_additional_word(self):
        input_data = ["eat", "tea", "tan", "ate", "nat", "bat", "tab"]
        expected_output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat', 'tab']]
        output = self.solution.groupAnagrams(input_data)
        output = [sorted(group) for group in output]
        expected_output = [sorted(group) for group in expected_output]
        self.assertEqual(sorted(output), sorted(expected_output))

    def test_group_anagrams_empty(self):
        input_data = []
        expected_output = []
        output = self.solution.groupAnagrams(input_data)
        self.assertEqual(output, expected_output)

    def test_group_anagrams_single_word(self):
        input_data = ["word"]
        expected_output = [["word"]]
        output = self.solution.groupAnagrams(input_data)
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()