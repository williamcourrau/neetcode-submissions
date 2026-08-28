# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        current = head

        length = 0

        while end:
            length += 1
            end = end.next
        
        prev = None
        pos_to_delete = length - n

        while pos_to_delete != 0:
            pos_to_delete -= 1
            prev = current
            current = current.next
        
        if prev is None:
            return head.next
        
        prev.next = current.next

        print(prev.val)

        return head
        