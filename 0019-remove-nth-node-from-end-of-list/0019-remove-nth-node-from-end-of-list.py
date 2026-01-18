# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # how many nodes do I have in the list
        # 1 -2- 3- 4 -5 -6 ## 2
        #          p   s      f
        #edge cases
        if not head or not head.next:
            return None

        dummy = ListNode(None)
        dummy.next = head

        fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        
        slow = dummy
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next


        