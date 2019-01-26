# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        low=head
        high=head
        while high and high.next:
            low=low.next
            high=high.next.next
            if low==high:
                return True
        return False
