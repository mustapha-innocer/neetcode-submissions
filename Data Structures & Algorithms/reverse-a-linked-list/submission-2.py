# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def rev(tail, head):
            if not head:
                return tail
            nextNode = head.next
            head.next = tail
            tail = head
            return rev(tail, nextNode)

        return rev(None, head)



        