# Use two pointers

class Solution:
    def trap(self, height):
        leftMax = 0
        rightMax = 0
        left = 0
        right = len(height) - 1
        trap = 0

        while left <= right:
            if leftMax <= rightMax:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    trap += leftMax - height[left]
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    trap += rightMax - height[right]
                right -= 1
        return trap


if __name__ == '__main__':
    s = Solution()
    rain = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(s.trap(rain))
