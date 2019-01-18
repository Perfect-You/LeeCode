class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            list_row=[]
            for j in range(9):
                if board[i][j]!=".":
                    num=board[i][j]
                    if num in list_row:
                        return False
                    else:
                        list_row.append(num)
                        
        for j in range(9):
            list_col=[]
            for i in range(9):
                if board[i][j]!=".":
                    num=board[i][j]
                    if num in list_col:
                        return False
                    else:
                        list_col.append(num)
                        
        box=[(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]
        for i,j in box:
            list_box=[]
            for m in range(-1,2):
                for n in range(-1,2):
                    if board[i-m][j-n]!=".":
                        num=board[i-m][j-n]
                        if num in list_box:
                            return False
                        else:
                            list_box.append(num)
        
        return True
