class Solution:
    def rotate(self, matrix):
        n = len(matrix[0])
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s = Solution()
    s.rotate(matrix)
    print(matrix)