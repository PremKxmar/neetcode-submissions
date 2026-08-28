# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        maxi=root.val
        def dfs(root,maxi):
            nonlocal count
            if not root:
                return 
        if root.val>=maxi:
            count+=1
            maxi=root.val

        left=dfs(root.left,maxi)
        right=dfs(root.right,maxi)
        
        dfs(root,root.val)
        return count

        