# Time: O(n), 52 ms
# Space: O(1), 8.3 MB

class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        last = 0
        for i in range(len(nums)):
            if nums[last] != nums[i]:
                last += 1
                nums[last] = nums[i]
        return last + 1

if __name__ == "__main__":
    print("026. Remove Duplicates from Sorted Array.")
    s = Solution()
    print("Test [1, 1, 2] and the expect result should be 2.")
    print(s.removeDuplicates([1, 1, 2]))