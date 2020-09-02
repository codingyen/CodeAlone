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

# Solution 3 Divide and Conquer
        """
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def work(i, j, K):
            if i >= j: return
            oi, oj = i, j
            pivot = dist(random.randint(i, j))
            while i < j:
                while i < j and dist(i) < pivot: i += 1
                while i < j and dist(j) > pivot: j -= 1
                points[i], points[j] = points[j], points[i]

            if K <= i - oi + 1:
                work(oi, i, K)
            else:
                work(i+1, oj, K - (i - oi + 1))

        work(0, len(points) - 1, K)
        return points[:K]
        """


if __name__ == '__main__':
    points = [[1,3],[-2,2]]
    K = 1
    s = Solution()
    print(s.kClosest(points, K))