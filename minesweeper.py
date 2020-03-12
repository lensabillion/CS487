class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return []

        row = len(board)
        col = len(board[0])
        i =  click[0] 
        j = click[1]
        directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        

        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
  
        def  dfs(i,j):
            if board[i][j] != 'E':
                return
            num_mine = 0
            for path in directions:
                next_i , next_j = i + path[0], j + path[1]
                if 0 <= next_i < row and 0 <= next_j < col and board[next_i][next_j] == 'M':
                    num_mine += 1
            if num_mine == 0:
                board[i][j] = 'B'
            else:
                board[i][j] =str(num_mine)
                return
            for path in directions:
                next_i , next_j = i + path[0], j + path[1]
                if 0 <= next_i < row and 0 <= next_j < col:
                    dfs(next_i,next_j)
        dfs(i,j)
        return board
                    
        
