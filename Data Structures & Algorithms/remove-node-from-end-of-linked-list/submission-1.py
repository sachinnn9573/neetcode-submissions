class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        left = dummy
        right = head

        # Move right pointer n positions
        while n > 0 and right:
            right = right.next
            n -= 1

        # Move both pointers until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the nth node
        left.next = left.next.next

        return dummy.next