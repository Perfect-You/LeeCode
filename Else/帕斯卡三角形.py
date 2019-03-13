class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return[[1],[1,1]]
        l=[[1],[1,1]]
        last=[1,1]
        for i in range(2,numRows):
            new=[1,1]
            for j in range(1,i):
                new.insert(j,last[j-1]+last[j])
            l.append(new)
            last=new
        return l
