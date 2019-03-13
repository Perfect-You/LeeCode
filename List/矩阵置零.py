'''遗憾的是，不是自己写的，这个方法实在是巧妙'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        row=False
        line=False
        for i in range(m):
            if matrix[i][0]==0:
                line=True
        for j in range(n):
            if matrix[0][j]==0:
                row=True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if line:
            for i in range(m):
                matrix[i][0]=0
        if row:
            for j in range(n):
                matrix[0][j]=0
