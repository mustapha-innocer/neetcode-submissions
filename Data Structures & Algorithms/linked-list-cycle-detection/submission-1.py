# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # nodes = set()
        # while head and head not in nodes:
        #     nodes.add(head)
        #     head = head.next
        # return head in nodes

        def check(nodes, head):
            if not head:
                return False
            if head in nodes:
                return True
            nodes.add(head)
            return check(nodes, head.next)

        return check(set(), head)
            
        