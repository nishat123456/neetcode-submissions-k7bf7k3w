# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #iterate through the list
        #find the value? 
        #skip w curr.next = curr.next.next
        dummy = ListNode(0)
        curr = dummy
        dummy.next = head

        if not head:
            return None
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next