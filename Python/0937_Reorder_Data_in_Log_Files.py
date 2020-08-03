"""
Space: O(l)
"""
class Solution:
    def reorderLogFiles(self, logs):
        let = [e for e in logs if e.split()[1:][0].isalpha()]
        dig = [e for e in logs if e.split()[1:][0].isdigit()]
        return (sorted(let, key = lambda x: [x.split()[1:], x.split()[0]])) + dig

if __name__ == "__main__":
     logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
     s = Solution()
     print(s.reorderLogFiles(logs))
