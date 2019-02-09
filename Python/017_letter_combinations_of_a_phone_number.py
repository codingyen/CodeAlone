# Time: O(n * 4^n), 32 ms
# Space: O(n), 6.5 MB

class Solution:
    def letterCombinations(self, digits: 'str') -> 'List[str]':
        # First, set up the dictionary for mapping
        lookup = [" ", " ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        sol = []
        # If no digits, return []
        if not digits:
            return []
        # Use DFS to solve
        self.dfs(0, "", digits, sol, lookup)
        return sol

    def dfs(self, depth, s, digits, sol, lookup):
        if depth == len(digits):
            sol.append(s)
            return
        else:
            for i in lookup[int(digits[depth])]:
                self.dfs(depth + 1, s + i, digits, sol, lookup)

if __name__ == "__main__":
    print("017 Letter Combinations of a Phone Number")
    print("Input 23 and the expect result should be ad, ae, af, bd, be, bf, cd, ce, cf")
    s = Solution()
    print(s.letterCombinations("23"))