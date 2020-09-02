class Solution:
    def myAtoi(self, str):
        INT_MAX = 2147483647
        INT_MIN =-2147483648
        result = 0

        str = str.strip()

        if not str:
            return result

        sign = 1
        if str[0] == '-' or str[0] == '+':
            if str[0] == '-':
                sign = -1
            str = str[1:]

        for i in str:
            if i <= '9' and i >= '0':
                result = result * 10 + ord(i) - ord('0')
            else:
                break

        if result > INT_MAX:
            if sign == 1:
                return INT_MAX
            else:
                return INT_MIN

        if sign == -1:
            result = 0 - result
        return result


        

if __name__ == "__main__":
    text = "   -42"
    s = Solution()
    print(s.myAtoi(text))
