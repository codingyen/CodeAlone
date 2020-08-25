class Solution:
    def lengthOfLongestSubstring(self, s):
        lookup = {}
        left = 0
        maxlen = 0
        for i in range(len(s)):
            if s[i] in lookup:
                left = max(left, lookup[s[i]] + 1)
            lookup[s[i]] = i
            maxlen = max(maxlen, i - left + 1)
        return maxlen


if __name__ == "__main__":
    c = "abccabcbb"
    s = Solution()
    print(s.lengthOfLongestSubstring(c))
