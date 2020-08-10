class Solution:
    def partitionLabels(self, S):
        lookup = {c: i for i, c in enumerate(S)}
        first, last = 0, 0
        result = []
        for i, c in enumerate(S):
            last = max(last, lookup[c])
            if i == last:
                result.append(i - first + 1)
                first = i + 1
        return result

if __name__ == '__main__':
    s = Solution()
    letters = "ababcbacadefegdehijhklij"
    print(s.partitionLabels(letters))