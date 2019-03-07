'''我写的，因为我一开始想到的就是排列组合公式,果然，时间效率太低了'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factorial(x):
            if x==0:
                return 1
            else:
                y=1
                for i in range(1,x+1):
                    y*=i
                return y
        i=0
        k=0
        result=0
        while i<int(n/2)+1:
            result+=factorial(n-k)/(factorial(i)*factorial(n-k-i))
            i+=1
            k+=1
        return result
'''这是别人写的，我都不知道是怎么想到的'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n ==2: return n
        
        a, b = 1, 2
        while n > 2:
            a, b = b, a + b
            n -= 1
        return b
