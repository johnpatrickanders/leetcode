# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))

    
# PLEASE AVOID UNNECESSARY DOUBLE CALL:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def validate(node, floor, ceil):
            if not node:
                return True
            if node.val <= floor or node.val >= ceil:
                return False
            return validate(node.left, floor, node.val) and validate(node.right, node.val, ceil)
        
        return validate(root.left, float("-inf"), root.val) and validate(root.right, root.val, float("inf"))
