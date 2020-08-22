# Time: O(n^3)
# Space: O(1)

class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        res = []

        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                # j - 1 could be i so it needs to be excluded.
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum = target - nums[i] - nums[j]
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] > sum:
                        right -= 1
                    elif nums[left] + nums[right] < sum:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

        return res


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    s = Solution()
    print(s.fourSum(nums, target))
