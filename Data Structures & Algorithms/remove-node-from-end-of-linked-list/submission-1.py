# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        if n == 1:
            prev = prev.next
        else:
            remove = prev
            for i in range(n - 2):
                remove = remove.next
            remove.next = remove.next.next


        curr1 = prev
        prev1 = None
        while curr1:
            temp1 = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = temp1

        return prev1
            
        