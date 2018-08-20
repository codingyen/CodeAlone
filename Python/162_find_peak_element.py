"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            # Finally left and right will be neighbot and one of them will be the peak.
            # if left value > right value, mid is left and right will become left.
            # if left value < rifht value, mid is left and left will become right.
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    s = Solution()
    print("Test case [1,2,3,1] and the result is ", s.findPeakElement([1, 2, 3, 1]))
    print("Test cae [1,2,1,3,5,6,4] and the result is ", s.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
