class Solution:
    def multiply(self, num1, num2):
        numlookUp = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        strlookUp = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        
        if num1 == '0' or num2 == '0':
            return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]
        tmpRes = [0 for i in range(len(num1) + len(num2))]

        for i in range(len(num1)):
            for j in range(len(num2)):
                tmpRes[i + j] += numlookUp[num1[i]] * numlookUp[num2[j]]
        
        res = [0 for i in range(len(num1) + len(num2))]
        
        for i in range(len(num1) + len(num2)):
            res[i] = tmpRes[i] % 10
            if i < len(num1) + len(num2) - 1:
                tmpRes[i + 1] += tmpRes[i] // 10

        return ''.join(strlookUp[i] for i in res[::-1]).lstrip('0')
        

if __name__ == "__main__":
    s = Solution()
    num1 = '6913259244'
    num2 = '71103343'
    print(s.multiply(num1, num2))