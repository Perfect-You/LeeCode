'''这个是自己写的，很遗憾，因为有很多循环吧，超出时间限制，逻辑上应该是没有问题'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def issame(str1,str2):
            if len(str1)!=len(str2):
                return False
            else:
                x=len(str1)
                for i in range(x):
                    if str1.count(str1[i])!=str2.count(str1[i]):
                        return False
            return True
        l=[]
        i=0
        while i<len(strs):
            new=[strs[i]]
            j=i+1
            while j<len(strs):
                if issame(strs[i],strs[j]):
                    new.append(strs[j])
                    del strs[j]
                else:
                    j+=1
            l.append(new)
            i+=1
        return l
