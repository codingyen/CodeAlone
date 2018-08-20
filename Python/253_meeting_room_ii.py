"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei)
find the minimum number of conference rooms required
"""

class Interval(object):
    def __init__(self, s = 0, e = 0):
         self.start = s
         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        
        starts.sort()
        ends.sort()
        
        # Create two pointers to indicate the specific start and end
        s, e = 0, 0
        minRoom, usedRoom = 0, 0
        
        while s < len(starts):
            if starts[s] < ends[e]:
                usedRoom += 1
                minRoom = max(minRoom, usedRoom)
                s += 1
            else:
                usedRoom -= 1
                e += 1
        return minRoom

if __name__ == "__main__":
    print("Start the test!")
    
    first = [Interval() for _ in xrange(3)]
    first[0].start = 0
    first[0].end = 30
    first[1].start = 5
    first[1].end = 10
    first[2].start = 15
    first[2].end = 20
    second = [Interval() for _ in xrange(2)]
    second[0].start = 7
    second[0].end = 10
    second[1].start = 2
    second[1].end = 4
    s = Solution()
    print(s.minMeetingRooms(first))
    print(s.minMeetingRooms(second))
