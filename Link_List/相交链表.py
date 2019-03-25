# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p=headA
        m=0
        q=headB
        n=0
        while p:
            p=p.next
            m+=1
        while q:
            q=q.next
            n+=1
        if p!=q:
            return None
        p=headA
        q=headB
        while m>n:
            p=p.next
            m-=1
        while n>m:
            q=q.next
            n-=1
        while p!=q:
            p=p.next
            q=q.next
        return p
