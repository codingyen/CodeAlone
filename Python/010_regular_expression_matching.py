"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

"""
# Solution 1
# Use dp
# Time:  O(n)
# Space: O(m * n)

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # Create a dictionary to store the status of i and j
	# i and j is the postition pointers of s and p
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    firstMatch = i < len(s) and p[j] in (s[i], '.')
                    # There are two situations if j is *
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or firstMatch and dp(i + 1, j)
                    else:
                        ans = firstMatch and dp(i + 1, j + 1)
                memo[i, j] = ans
            return memo[i, j]	
        # Start from the position 0 for both
        return dp(0, 0) 

if __name__ == "__main__":
    print("Start the test!")
    print(Solution().isMatch("aa", "a"))
    print(Solution().isMatch("aa","aa"))
