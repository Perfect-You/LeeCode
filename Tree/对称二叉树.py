# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def symmetry(x,y):
            if x==None:
                return y==None
            if y==None:
                return x==None
            if x.val==y.val:
                return symmetry(x.left,y.right) and symmetry(x.right,y.left)
            if x.val!=y.val:
                return False
            
        if root==None:
            return True
        return symmetry(root.left,root.right)
