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
        # Step 1: Finding the center of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        temp = slow.next
        prev = slow.next = None
        while temp:
            node = temp.next
            temp.next = prev
            prev = temp
            temp = node
        
        # Step 3: Alternatively add both of them one by one
        first, second = head, prev
        while second:
            temp = first.next
            node = second.next
            first.next = second
            second.next = temp
            first = temp
            second = node