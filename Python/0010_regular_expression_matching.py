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
# Time:  O(m * n), 52 ms
# Space: O(m * n), 6.9 MB

class Solution1:
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
class Solution2:
    # Time: O((s + p) * 2 ^ (s + p)), 928 ms
    # Space: O(s + p), 6.5 MB
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        # Base case
        if not p:
            return not s
        # Note that we need to consider if the length of p is 1 first
        # Otherwise, p[1] will return error if the length of p is 1
        if len(p) == 1 or p[1] != '*':
            # Need to check if len(s) > 0 first
            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            while len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                if self.isMatch(s, p[2:]):
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])

if __name__ == "__main__":
    print("Start the test!")
    s = Solution1()
    print("Test \"aa\" and \"a\" and the expect reuslt is False!")
    print(s.isMatch("aa", "a"))
    print("Test \"aa\" and \"aa\" and the expect reuslt is True!")
    print(s.isMatch("aa","aa"))
    print("Test \"ab\" and \".*\" and the expect reuslt is True!")
    print(s.isMatch("ab",".*"))
    print("Test \"aab\" and \"c*a*b\" and the expect reuslt is True!")
    print(s.isMatch("aab","c*a*b"))
    print("Test \"mississippi\" and \"mis*is*p*\" and the expect reuslt is False!")
    print(s.isMatch("mississippi","mis*is*p*"))
    print("Test \"ab\" and \".*c\" and the expect reuslt is False!")
    print(s.isMatch("ab",".*c"))