class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=[]
        for i in s.lower():
            if i.isalnum():
                l.append(i)
        return l==l[::-1]
