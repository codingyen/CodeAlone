# Time: O(n), 36 ms
# Space: O(n), 6.5 MB

class Solution:
    def isValid(self, s: 'str') -> 'bool':
        stack, lookup = [], {"(" : ")", "{" : "}", "[" : "]"}
        for i in s:
            if i in lookup:
                stack.append(i)
            elif len(stack) == 0 or lookup[stack.pop()] != i:
                return False
        return len(stack) == 0

if __name__ == "__main__":
    print("020. Valid Parentheses")
    s = Solution()
    print("Input: () and the expect result should be true.")
    print(s.isValid("()"))
    print("Input: ()[]{} and the expect result should be true.")
    print(s.isValid("()[]{}"))
    print("Input: (} and the expect result should be False.")
    print(s.isValid("(}"))