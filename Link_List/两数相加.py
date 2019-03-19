# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        re=ListNode(0)
        first=re
        firstnum=0
        while True:
            if l1!=None:
                firstnum+=l1.val
                l1=l1.next
            if l2!=None:
                firstnum+=l2.val
                l2=l2.next
            first.val=firstnum%10
            firstnum=int(firstnum/10)
            if l1==None and l2==None and firstnum==0:
                break
            first.next=ListNode(0)
            first=first.next
            
        return re
