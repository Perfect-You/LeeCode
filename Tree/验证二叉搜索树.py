# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res=[]
        self.isorder(root,res)
        if res!=sorted(list(set(res))):
            return False
        else:
            return True
        
    def isorder(self,root,res):
        if root==None:
            return []
        self.isorder(root.left,res)
        res.append(root.val)
        self.isorder(root.right,res)
        return res
