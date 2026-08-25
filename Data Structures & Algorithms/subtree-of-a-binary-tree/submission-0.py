# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if sametree(root,subRoot):
            return sametree(root.left,subRoot.left) and sametree(root.right,subRoot.right)
        else:
            return False 

        def sametree(root,subtree):
            if not root and not subtree:
                return False
            if root and subtree and root.val==subtree.val:
                return sametree(root.left,subtree.left) and subtree(root.right,subtree.right)

            else:
                return False