# Time: O(n), 116 ms
# Space: O(1), 6.9 MB

class Solution1:
    def romanToInt(self, s: 'str') -> 'int':
        mapping = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        sum = 0
        for i in range(len(s)):
            if i > 0 and mapping[s[i]] > mapping[s[i - 1]]:
                sum += mapping[s[i]] - 2 * mapping[s[i - 1]]
            else:
                sum += mapping[s[i]]
        return sum

if __name__ == "__main__":
    print("013. Roamn to Integer")
    s = Solution1()
    print("Test III and the expect result is 3")
    print(s.romanToInt("III"))
    print("Test IV and the expect result is 4")
    print(s.romanToInt("IV"))
    print("Test IX and the expect result is 9")
    print(s.romanToInt("IX"))
    print("Test LVIII and the expect result is 58")
    print(s.romanToInt("LVIII"))
    print("Test MCMXCIV and the expect result is 1994")
    print(s.romanToInt("MCMXCIV"))