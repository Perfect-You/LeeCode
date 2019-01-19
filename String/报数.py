class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        new_s='1'
        if n==2:
            new_s='11'
        s='11'
        for i in range(3,n+1):
            new_s=''
            count=1
            for j in range(1,len(s)):
                if s[j]==s[j-1]:
                    count+=1
                else:
                    new_s+=str(count)+s[j-1]
                    count=1
            new_s+=str(count)+s[j]
            s=new_s
        return new_s
