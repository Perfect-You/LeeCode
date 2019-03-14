class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        m=a^b
        n=(a&b)<<1
        return sum([m,n])
