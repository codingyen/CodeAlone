# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Search in array one by one
        # Time: O(n ^ 2), 4608 ms
        # Space: O(n), 7.2 MB
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums, target):
        # Use Hash Table
        # Time: O(n), 40 ms
        # Space: O(n), 7.8 MB
        dic = {}
        for i, j in enumerate(nums):
            if target - j in dic: # This check if target - j as a key in the dic or not
                return [dic[target - j], i]
            dic[j] = i # As a result, we need to save value as a key

if __name__ == "__main__":
    print("001. Two Sum")
    s = Solution()
    print(s.twoSum2([2, 7, 11, 15], 9))
    print("The result should be [0, 1]")
    print(s.twoSum2([3, 2, 4], 6))
    print("The result should be [1, 2]")