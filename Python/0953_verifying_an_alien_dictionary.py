class Solution:
    def isAlienSorted(self, words, order):
        lookup = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if lookup[word1[j]] > lookup[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True

if __name__ == '__main__':
    words = ["apap","app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    s = Solution()
    print(s.isAlienSorted(words, order))