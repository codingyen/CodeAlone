class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self. right = right

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isChildSymmetric(root.left, root.right)

    def isChildSymmetric(self, left, right):
        if not left and not right:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isChildSymmetric(left.left, right.right) and self.isChildSymmetric(left.right, right.left)


if __name__ == "__main__":
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(2)
    l4 = TreeNode(3)
    l5 = TreeNode(4)
    l6 = TreeNode(4)
    l7 = TreeNode(3)
    
    l1.left = l2
    l1.right = l3

    l2.left = l4
    l2.right = l5

    l3.left = l6
    l3.right = l7

    s = Solution()
    print(s.isSymmetric(l1))