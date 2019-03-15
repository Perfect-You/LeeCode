'''这个应该是最容易想到的办法了，但是很遗憾，会超出时间限制'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        x=1
        for i in range(n):
            x=x*n
            n-=1
        y=str(x)
        m=len(y)
        z=0
        for i in range(m):
            if y[m-i-1]=="0":
                z+=1
            else:
                break
        return z
'''这个是别人的，喵的！我怎么想不到'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        x=0
        while n>=5:
            n=n//5
            x+=n
        return x
