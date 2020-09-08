class Solution:
    def nextPermutation(self, nums):
        right = len(nums) - 1
        while right >= 0:
            if nums[right] > nums[right - 1]:
                nums[right:] = sorted(nums[right:])
                for i in range(right, len(nums)):
                    if nums[i] > nums[right - 1]:
                        nums[right - 1], nums[i] = nums[i], nums[right - 1]
                        break
                break
            right -= 1
        return nums

if __name__ == "__main__":
    nums = [3, 2, 1]
    s = Solution()
    print(s.nextPermutation(nums))