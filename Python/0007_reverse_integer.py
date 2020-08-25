class Solution:
    def reverse(self, x):
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        
        result = 0

        while x:
            result = result * 10 + x % 10
            x //= 10
        result = sign * result
        return result if result < 2 ** 31 and result > -(2 ** 31) else 0
        

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))