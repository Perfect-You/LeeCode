class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:          #如果s[i]的值等于t[j]的值，i和j同时加一，不然的话，j+1
                i+=1
                j+=1
            else:
                j+=1
        if i<len(s):           #在跳出循环之前，i加了一，所以得到的i应该是等于len(s)的
            return False
        else:
            return True
