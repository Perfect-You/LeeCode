class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        m=list(str(bin(x))[2:])
        n=list(str(bin(y))[2:])
        l=max(len(m),len(n))+1
        if len(m)<l:
            m=['0']*(l-len(m))+m
        if len(n)<l:
            n=['0']*(l-len(n))+n
        print(m,n)
        count=0
        for i in range(l):
            if m[i]!=n[i]:
                count+=1
        return count
