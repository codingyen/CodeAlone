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

"""
Solution 2
Use recursive
Base Case
if not p, return not s 
Recursion:
Case Analysis
s[0] s[1]
p[0] p[1] p[2]

Case 1: When p[1] != '*' or len(p) == 1,
        if s[0] == p[0] or (len(s) > 0 and p[0] == '.') 
            return isMatch(s[1:], p[1:])
        else
            return False
Case 2: When p[1] == '*', keep moving the checking for s to the rightmost
        while len(s) > 0 and s[0] == p[0] or p[0] == '.':
            if isMatch(s, p[2:])
                return True
            s = s[1:]
        isMatch(s, p[2:]) => Need to check the last time!
"""

if __name__ == "__main__":
    print("Start the test!")
    s = Solution()
    print("Test \"aa\" and \"a\" and the expect reuslt is False!")
    print(s.isMatch("aa", "a"))
    print("Test \"aa\" and \"aa\" and the expect reuslt is True!")
    print(s.isMatch("aa","aa"))
