"""

Given a time represented in the format "HH:MM", 
form the next closest time by reusing the current digits.
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid.
For example, "01:34", "12:09" are all valid.
"1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, 
which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.

Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller
than the input time numerically.

Time:  O(1)
Space: O(1)

"""
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        # First, separate the hour and minute
        h = int(time[0:2])
        m = int(time[3:5])
        # Store s as a set for the next comparison (Tricky Part!)
        s = set(time)
        # Within one day, all the possible combination should be checked.
        for _ in xrange(1441):
            m += 1
            if m == 60:
                m = 0
                if h == 23:
                    h = 0
                else:
                    h += 1
            # 02d formats an integer (d) to a field of minimum width 2 (2), 
            # with zero-padding on the left (leading 0)
            time = "%02d:%02d" % (h, m)
            if set(time) <= s:
                break
        return time


if __name__ == "__main__":
    print("Start the test!")
    s = Solution()
    testTime1 = "19:34"
    testTime2 = "01:32"
    print("Test with 19:34. Answer is 19:39. Result is %s" % s.nextClosestTime(testTime1))
    print("Test with 01:32. Answer is 01:33. Result is %s" % s.nextClosestTime(testTime1))
