# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 3 4 9
        # 5 6 2
        dummy = ListNode(0)
        current = dummy
        remainder = 0

        while l1 or l2:
            if l1 and l2:
                summ = l1.val + l2.val + remainder # 11
                if summ >= 10:
                    quotient = summ % 10 #1
                else:
                    quotient = summ
                l1 = l1.next
                l2 = l2.next

            elif l1:
                summ = l1.val + remainder
                quotient = summ % 10
                l1 = l1.next
            else:
                summ = l2.val + remainder
                quotient = summ % 10
                l2 = l2.next

            remainder = summ // 10 #1
            current.next = ListNode(quotient)
            current = current.next
        
        if remainder:
            current.next = ListNode(remainder)
        
        return dummy.next


        
        