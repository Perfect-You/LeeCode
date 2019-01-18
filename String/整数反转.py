class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            x=0-x
            s=str(x)
            s=s[::-1]
            s.lstrip('0')
            i=-int(s)
            if i<-2**31:
                return 0
            else:
                return i
        else:
            s=str(x)
            s=s[::-1]
            s.lstrip('0')
            n=int(s)
            if n>2**31-1:
                return 0
            else:
                return n
