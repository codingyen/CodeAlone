class Solution:
    def maxSubArray(self, nums):
        result, curr = float("-inf"), float("-inf")
        for i in nums:
            curr = max(curr + i, i)
            result = max(curr, result)
        return result

if __name__ == "__main__":
    a = [-2, -3, 9, -1, 7]
    s = Solution()
    print(s.maxSubArray(a))