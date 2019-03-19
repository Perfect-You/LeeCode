'''因为用了两层循环，会超出时间限制，啊啊啊啊'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def ispalindrome(s):
            l=[]
            for i in s:
                l.append(i)
            return l==l[::-1]
        l=""
        lnew=""
        i=0
        j=0
        while i<len(s):
            j=i
            while j<len(s):
                lnew=lnew+s[j]
                if ispalindrome(lnew) and len(lnew)>len(l):
                    l=lnew
                j=j+1
            lnew=""
            i=i+1
        return l
