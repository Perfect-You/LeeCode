class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l=len(needle)
        if l==0:
            return 0
        else:
            for i,ch in enumerate(haystack):
                if i+l>len(haystack):
                    break
                if haystack[i:i+l]==needle:
                    return i
            return -1
