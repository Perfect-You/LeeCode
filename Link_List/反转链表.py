# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp=0
        p=head
        length=0
        while p:
            length+=1
            p=p.next
        p=head
        n=length-1
        for i in range(length-1):
            for j in range(n):
                temp=p.val
                p.val=p.next.val
                p.next.val=temp
                p=p.next
            n=n-1
            p=head
        return head
'''chage'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre=None
        cur=head
        while cur:
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        return pre
