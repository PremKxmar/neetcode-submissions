# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(p,q):
            if not p and not q:
                return True
            if p.val and q.val and p.val==q.val:
                return sametree(p.left,q.left) and sametree(p.right,q.right)
            else:
                return False

        if not root:
            return False
        if not subRoot:
            return True
            
        if sametree(root,subRoot):
            return True
        left=self.isSubtree(p.left,q.left)
        right=self.isSubtree(p.right,q.right)
        return left or right
        