class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        most = 0
        while left < right:
            if height[left] <= height[right]:
                water = height[left] * (right - left)
                left += 1
            else:
                water = height[right] * (right - left)
                right -= 1
            most = max(most, water)
        return most


if __name__ == "__main__":
    heightList = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    print(s.maxArea(heightList))




