"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Solution : Copy the state and work on it. Then copy the new state to answer. 
            Time complexity : O(MN)
            Space complexity : O(MN) - Since copying the whole board

        O(1) Space solution -> use additional states like -1 and 2
                                0 - prev 0 cur 0
                                1 - prev 1 cur 1
                                2 - prev 0 now 1
                                -1 - prev 1 now 0

                                Once you have done the changes, return the original board with current states only

        TODO - Infinite board??/ Sparse board??
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(i,j):
            if i< 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            return True
        
        def update(cur):
            #copy solution
            new_board = [x[:] for x in cur]
            neighbours = [[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,-1],[1,0],[1,1]]
            for i in range(0,len(cur)):
                for j in range(0,len(cur[0])):
                    #check neighbours and update on new_board
                    live = False
                    if cur[i][j]:
                        live= True
                    live_neighs = 0
                    x = [[n[0] + i,n[1] + j] for n in neighbours]
                    for n in neighbours:
                        k, l = i + n[0], j+ n[1]
                        if valid(k,l) and cur[k][l]:
                            live_neighs+=1 
                    if live and live_neighs < 2:                        
                        new_board[i][j] = 0
                    elif live and (live_neighs ==2 or live_neighs ==3):                        
                        new_board[i][j] = 1
                    elif live and live_neighs >3:
                        new_board[i][j] = 0
                    elif (( not live) and live_neighs == 3):
                        new_board[i][j] = 1
                    else:
                        new_board[i][j] = cur[i][j]
            #update cur
            flag = False
            for i in range(0,len(cur)):
                for j in range(0,len(cur[0])):
                    if cur[i][j]!=new_board[i][j]:
                        flag = True
                    cur[i][j] = new_board[i][j]
            return flag
        
        update(board)

    def gameOfLifeO1(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid(i,j):
            if i< 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            return True
                
        def update(cur):
            #additional states solution
            neighbours = [[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,-1],[1,0],[1,1]]
            for i in range(0,len(cur)):
                for j in range(0,len(cur[0])):
                    #check neighbours and update on new_board
                    live = False
                    if cur[i][j]:
                        live= True
                    live_neighs = 0
                    x = [[n[0] + i,n[1] + j] for n in neighbours]
                    for n in neighbours:
                        k, l = i + n[0], j+ n[1]
                        if valid(k,l) and abs(cur[k][l]) == 1:
                            live_neighs+=1 
                    if live and live_neighs < 2:                        
                        cur[i][j] = -1
                    elif live and (live_neighs ==2 or live_neighs ==3):                        
                        cur[i][j] = 1
                    elif live and live_neighs >3:
                        cur[i][j] = -1
                    elif (( not live) and live_neighs == 3):
                        cur[i][j] = 2
            
            #final board
            for i in range(0,len(cur)):
                for j in range(0,len(cur[0])):
                    if cur[i][j]>0:
                        cur[i][j] = 1
                    else:
                        cur[i][j] = 0
        
        update(board)