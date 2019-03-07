# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        j=n
        i=2
        while j>0:
            if isBadVersion(j)==True and isBadVersion(j-1)==False:
                break
            else:
                if isBadVersion(j):
                    j=j-int(n/i)
                    i+=1
                if not isBadVersion(j):
                    j=j+int(n/i)
                    i+=1
        return j
