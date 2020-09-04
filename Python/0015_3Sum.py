class Solution:
    def threeSum(self, nums):
        res = []
        nums = sorted(nums)
        
        for i in range(len(nums) - 2):
            # if nums[i] > 0 then there is no chance to get the sum to 0
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                start = i + 1
                end = len(nums) - 1
                while start < end:
                    if nums[i] + nums[start] + nums[end] < 0:
                        start += 1
                    elif nums[i] + nums[start] + nums[end] > 0:
                        end -= 1
                    else:
                        res.append([nums[i], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        # start cannot be the same as well.
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
        return res

if __name__ == "__main__":
    nums = [0, 0, 0, 0]
    s = Solution()
    print(s.threeSum(nums))