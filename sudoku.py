
'''
Sudoku Solver  
A terminal-based Sudoku solver using the backtracking algorithm.  
Empty cells are represented by 0. The program fills in valid values recursively.
'''
def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-"*21)
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(num if num != 0 else ".", end=" ")
        print()

def is_valid(board, num, pos):
    row, col = pos
    # Check row
    if num in board[row]: return False
    # Check column
    if num in [board[i][col] for i in range(9)]: return False
    # Check 3x3 box
    box_x, box_y = col // 3, row // 3
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, (i, j)):
                        board[i][j] = num
                        if solve(board): return True
                        board[i][j] = 0
                return False
    return True

# Sample Sudoku puzzle
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

print("Initial Sudoku:")
print_board(board)
solve(board)
print("\nSolved Sudoku:")
print_board(board)

