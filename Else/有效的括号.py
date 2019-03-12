class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                l.append(i)
            if i==")":
                if len(l)==0 or l[-1]!="(":
                    return False
                else:
                    l.pop()
            if i=="]":
                if len(l)==0 or l[-1]!="[":
                    return False
                else:
                    l.pop()
            if i=="}":
                if len(l)==0 or l[-1]!="{":
                    return False
                else:
                    l.pop()
        return len(l)==0
