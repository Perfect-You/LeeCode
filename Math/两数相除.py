'''遗憾的是，时间会超出期限，喵！'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative=False
        if dividend<0 and divisor>0 or dividend>0 and divisor<0:
            negative=True
        x=abs(dividend)
        y=abs(divisor)
        re=0
        while x>=y:
            x=x-y
            re+=1
        if negative:
            re=0-re
        if re>2**31-1:
            re=2**32-1
        return re    
'''啦啦啦，新的来啦，注意range和xrange的差别'''
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative=1
        if dividend<0 and divisor>0 or dividend>0 and divisor<0:
            negative=-1
        x=abs(dividend)
        y=abs(divisor)
        if y==1:
            return negative*x if negative*x < 2**31 else 2**31-1
        if x<y:
            return negative*0
        if x==y:
            return negative*1
        re=len(xrange(y,x,y))
        if (re+1)*y==x:
            re+=1
        return negative*re
