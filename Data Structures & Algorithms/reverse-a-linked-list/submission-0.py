# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        tail = head
        curr = head.next
        tail.next = None
        while curr:
            nextNode = curr.next
            curr.next = tail
            tail = curr
            curr = nextNode
        return tail


        