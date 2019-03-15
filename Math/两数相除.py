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
