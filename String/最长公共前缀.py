class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l=''
        x=[]
        if len(strs)>0:
            for i in range(len(strs)):
                x.append(len(strs[i]))
            n=min(x)
            for i in range(n):
                count=0
                for j in range(len(strs)):
                    if strs[j][i]==strs[j-1][i]:
                        count+=1
                    else:
                        break
                if count==len(strs):
                    l+=strs[j][i]
                else:
                    break
        return l
