class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left= 0
        right = 0
        mx = 0
        st = set()
        while right < len(s):
            if s[right] in st:
                while s[right] in st:
                    st.remove(s[left])
                    left += 1
            else:
                st.add(s[right])
                right += 1
                mx = max(right - left, mx)
        return mx
        