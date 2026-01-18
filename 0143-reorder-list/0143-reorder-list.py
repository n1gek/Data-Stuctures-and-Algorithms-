# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(None)
        fast = slow = dummy
        dummy.next = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        new = slow.next
        slow.next = None

        def reverse(node):
            prev = None
            curr = node

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
        
            return prev

        headA, headB = head, reverse(new)
        print(headB)
        #1 2 3
        #    |
        #5 4
        #     |
        # dummy - 1 - 5 - 2 - 4

        dummy = ListNode(None)
        curr = dummy
        while headA and headB:
            curr.next = headA
            headA = headA.next
            curr = curr.next

            curr.next = headB
            headB = headB.next
            curr = curr.next
        
        if headA:
            curr.next = headA
        if headB:
            curr.next = headB
        
        return dummy.next

        