# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        if head.next==None:
            return head
        o=head.next
        p=o
        j=head
        i=o.next
        x=3
        while i!=None:
            if x%2!=0:
                j.next=i
                j=j.next
                i=i.next
                x+=1
            else:
                o.next=i
                o=o.next
                i=i.next
                x+=1
        j.next=p
        o.next=None
        return head
