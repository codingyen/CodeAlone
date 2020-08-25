# What is the time complexity?
# What is the space complexity?

class Solution:
    def generateParenthesis(self, n):
        ans = []
        self.helper(n, ans, '', left = 0, right = 0)
        return ans

    def helper(self, n, ans, s, left, right):
        if len(s) == 2 * n:
            ans.append(s)
            return
        if left < n:
            self.helper(n, ans, s + '(', left + 1, right)
        if right < left:
            self.helper(n, ans, s + ')', left, right + 1)


if __name__ == "__main__":
    y = Solution()
    print(y.generateParenthesis(3))
