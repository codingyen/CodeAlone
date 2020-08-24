class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False
            return helper(node.left, lower, val) and helper(node.right, val, upper)

        return helper(root)


if __name__ == "__main__":
    l1 = TreeNode(1)
    l2 = TreeNode(1)
    #l3 = TreeNode(3)
    #l4 = TreeNode(3)
    #l5 = TreeNode(6)

    root = l1
    l1.left = l2
    #l1.right = l3
    #l3.left = l4
    #l3.right = l5

    s = Solution()
    print(s.isValidBST(root))


