class Solution:
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        longest_seq = 0

        for num in nums_set:
            # Don't need to check if there is a - 1 smaller in the list. 
            if num - 1 not in nums_set: 
                current_num = num
                current_seq = 1

                while current_num + 1 in nums_set:
                    current_num += 1
                    current_seq += 1

                longest_seq = max(longest_seq, current_seq)

        return longest_seq


if __name__ == '__main__':
    s = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(s.longestConsecutive(nums))
