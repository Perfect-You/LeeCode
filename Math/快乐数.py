class Solution:
    def isHappy(self, n: int) -> bool:
        def square(x):
            s=str(x)
            l=list(s)
            n=0
            for i in range(len(l)):
                n+=int(l[i])**2
            return n
        i=0
        while i<1000:
            n=square(n)
            if n==1:
                return True
            i+=1
        return False
