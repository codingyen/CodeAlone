class Solution:
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res


    def helper(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        return s[j + 1 : k]


if __name__ == '__main__':
    ss = "babad"
    s = Solution()
    print(s.longestPalindrome(ss))