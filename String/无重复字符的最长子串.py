class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longnum=0
        l=[]
        i=0
        j=0
        while i<len(s) and j<len(s):
            if s[j] not in l:
                l.append(s[j])
                if len(l)>longnum:
                    longnum=len(l)
                j+=1
            else:
                l=[]
                i+=1
                j=i
            
        
        return longnum
