# Add continuous sum to hash table
# Ex. [1, 1, 1] => d{0: 1, 1: 1, 2: 1, 3: 1}
# If current sum - k is in d, then we know current sum + d[sum - k] = k

from collections import defaultdict

class Solution:
    def subarraySum(self, nums, k):
        n = len(nums)
        d = defaultdict(int)
        d[0] = 1
        sum = 0
        res = 0
        for i in range(n):
            sum += nums[i]
            if sum - k in d:
                res += d[sum - k]
            d[sum] += 1
        return res


if __name__ == "__main__":
    nums = [0, 0, 0]
    k = 0
    s = Solution()
    print(s.subarraySum(nums, k))