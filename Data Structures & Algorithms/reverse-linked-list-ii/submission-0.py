# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        left_prev=dummy
        curr=head
        for _ in range(left-1):
            prev_left=curr
            curr=curr.next
        prev=None
        for _ in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        prev_left.next=prev
        prev_left.next.next=curr
        return dummy.next