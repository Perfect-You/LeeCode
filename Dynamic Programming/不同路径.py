class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(x):
            re=1
            while x>0:
                re*=x
                x-=1
            return re
        x=m+n-2
        y=m-1
        z=n-1
        re=factorial(x)/(factorial(y)*factorial(z))
        return int(re)
