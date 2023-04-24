class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = []
        def traverse(board, row, col, prev, newv):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return
            
            if board[row][col] != prev:
                return
            
            board[row][col] = newv
            
            traverse(board, row + 1, col, prev, newv)
            traverse(board, row - 1, col, prev, newv)
            traverse(board, row, col + 1, prev, newv)
            traverse(board, row, col - 1, prev, newv)
            
        def find(board):
            M , N = len(board), len(board[0])
            for i in range(M):
                for j in range(N):
                    if (board[i][j] == 'O'):
                        board[i][j] = '-'
            for i in range(M):
                if (board[i][0] == '-'):
                    traverse(board, i, 0, '-', 'O')
            
            for i in range(M):
                if (board[i][N - 1] == '-'):
                    traverse(board, i, N - 1, '-', 'O')
            for i in range(N):
                if (board[0][i] == '-'):
                    traverse(board, 0, i, '-', 'O')
            for i in range(N):
                if (board[M - 1][i] == '-'):
                    traverse(board, M - 1, i, '-', 'O')
                    
            for i in range(M):
                for j in range(N):
                    if (board[i][j] == '-'):
                        board[i][j] = 'X'
        find(board)