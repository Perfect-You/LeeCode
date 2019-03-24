'''是别人写的，我自己写的大概也是这个思路，但是没有这个巧妙，总是有各种错误'''
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = end = 0
        
        for i in range(len(s)):
            len1 = self.centerexpand(s, i, i)   #回文串长度为奇数，aba
            len2 = self.centerexpand(s, i, i+1)  #回文串长度为偶数，abba
            maxlen = max(len1, len2)
            if maxlen > end - start + 1:
                start = i - (maxlen - 1)//2
                end = i + maxlen//2
        return s[start: end+1]
                
    def centerexpand(self,s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1
