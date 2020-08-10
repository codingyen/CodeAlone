import heapq

class Solution:
    def kClosest(self, points, K):

# Solution 1
        """
        def dist(point):
            return point[0] ** 2 + point[1] ** 2
        
        maxheap = []
        
        for point in points:
            heapq.heappush(maxheap, (dist(point), point))
        
        return [heapq.heappop(maxheap)[1] for _ in range(K)]
        """

# Solution 2
        points.sort(key = lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]



if __name__ == '__main__':
    points = [[1,3],[-2,2]]
    K = 1
    s = Solution()
    print(s.kClosest(points, K))