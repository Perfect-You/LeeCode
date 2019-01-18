class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                x=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=x
        
        for i in range(n):
            matrix[i]=matrix[i][::-1]
