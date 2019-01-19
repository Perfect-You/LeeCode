# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p=head
        index=0
        length=0
        while p:
            length+=1
            p=p.next
        p=head
        x=length-n
        if x==0:
            return p.next
        for i in range(length):
            if i==x-1:
                p.next=p.next.next
                return head
            else:
                p=p.next
