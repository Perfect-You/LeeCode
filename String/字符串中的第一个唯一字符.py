class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        str="abcdefghigklmnopqrstuvwxyz"
        l=[]
        for i in str:
            if s.find(i)==s.rfind(i) and s.find(i)!=-1:
                l.append(s.find(i))
        if len(l)>0:
            return min(l)
        else:
            return -1
