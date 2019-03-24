class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        re=[]
        for i in range(numRows):
            re.append([])
        n=len(re)-1
        i=0
        while i<len(s):
            for j in range(2*n):
                if i>=len(s):
                    break
                if j<=n:
                    re[j].append(s[i])
                    j+=1
                    i+=1
                else:
                    re[2*n-j].append(s[i])
                    j+=1
                    i+=1
        r=""
        for i in range(len(re)):
            r+=''.join(re[i])
        return r
            
