class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=digits
        a[-1]+=1
        for n in range(len(a)):
            for i in range(len(a)):
                if a[i]==10:
                    if i!=0:
                        a[i]=0
                        a[i-1]+=1
                    if i==0:
                        a[i]=0
                        a.insert(0,1)
        return a
