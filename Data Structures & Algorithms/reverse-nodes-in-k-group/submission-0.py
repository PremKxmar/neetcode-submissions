# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        group_prev=dummy

        while True:
            kth=group_prev
            for _ in range(k):
                kth=kth.next
                if not kth:
                    break
            if not kth:
                break
            group_first=group_prev.next
            curr=group_first
            prev=kth.next
            for _ in range(k):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            group_prev.next=prev
            group_prev=group_first
        return dummy.next
            
            
                