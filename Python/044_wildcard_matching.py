"""
Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Time: O(m + n)
Space: O(1)

"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sP, pP, tP = 0, 0, 0
        star = -1

        while sP < len(s):
            if pP < len(p) and p[pP] in (s[sP], '?'):
                sP += 1
                pP += 1
                continue
            if pP < len(p) and p[pP] == '*':
                star = pP
                pP += 1
                tP = sP
                continue
            if star != -1:
                pP = star + 1
                tP += 1
                sP = tP
                continue
            return False

        while pP < len(p) and p[pP] == '*':
            pP += 1

        if pP == len(p):
            return True
        return False


if __name__ == "__main__":
    print("Start the test!")
    print(Solution().isMatch("aa", "a"))
    print(Solution().isMatch("aa","aa"))
    print(Solution().isMatch("aaa","aa"))
    print(Solution().isMatch("aa", "a*"))
    print(Solution().isMatch("aa", "?*"))
    print(Solution().isMatch("ab", "?*"))
    print(Solution().isMatch("aab", "c*a*b"))
