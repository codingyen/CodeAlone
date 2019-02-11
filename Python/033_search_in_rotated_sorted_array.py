# Time: O(logn)
# Space: O(1)
class Solution:
    def search(self, nums: 'Lists[int]', target: 'int') -> 'int':
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif (nums[left] <= nums[mid] and nums[left] <= target < nums[mid]) or (nums[left] > nums[mid] and not (nums[mid] < target <= nums[right])):
                right = mid - 1
            else:
                left =  mid + 1
        return -1

if __name__ == "__main__":
    print("033. Search in Rotated Sorted Array")
    s = Solution()
    print("Test nums = [4, 5, 6, 7, 0, 1, 2] and target = 0. The expect result should be 4")
    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))
    print("Test nums = [4, 5, 6, 7, 0, 1, 2] and target = 3. The expect result should be -1")
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
