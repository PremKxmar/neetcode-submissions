# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        prev=None
        curr=root
        while curr and curr.val!=key:
            prev=curr
            if key>curr.val:
                curr=curr.right
            else:
                curr=curr.left
        if not curr:
            return root
        
        if not curr.right or not curr.left:
            child=curr.right if curr.right else curr.left
            
            if root.val==key:
                return child

            if prev.left==curr:
                prev.left=child
            else:
                prev.right=child
        
        else:
            succ_parent=curr
            succ=curr.right
            while succ.left:
                succ_parent=succ
                succ=succ.left
            curr.val=succ.val

            if succ_parent.left==succ:
                succ_parent.left=succ.right
            else:
                succ_parent.right=succ.right
        return root

                



