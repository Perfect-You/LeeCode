class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.strip()
        s={i for i in '0123456789'}
        negative=False
        x=0
        if len(str)==0:
            return 0
        if str[0]=='-':
            negative=True
        if str[0]=='-' or str[0]=='+':
            str=str[1:]
        
        for i in str:
            if i not in s:
                break
            x=x*10+int(i)
        if negative:
            x=-x
        if x>2**31-1:
            return 2**31-1
        if x<-2**31:
            return -2**31
        else:
            return x
