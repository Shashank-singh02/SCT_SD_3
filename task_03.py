def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using backtracking.
    Modifies the board in-place.
    """
    find = find_empty(board)
    if not find:
        return True  
    else:
        row, col = find

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0  

    return False

def find_empty(board):
    """
    Finds the next empty cell (represented by 0) in the board.
    Returns (row, col) or None if no empty cell is found.
    """
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None

def is_valid(board, num, pos):
    """
    Checks if placing 'num' at 'pos' (row, col) is valid.
    """
    row, col = pos

  
    for c in range(9):
        if board[row][c] == num and col != c:
            return False

    
    for r in range(9):
        if board[r][col] == num and row != r:
            return False

    
    box_x = col // 3
    box_y = row // 3

    for r in range(box_y * 3, box_y * 3 + 3):
        for c in range(box_x * 3, box_x * 3 + 3):
            if board[r][c] == num and (r, c) != pos:
                return False
    return True

def print_board(board):
    """
    Prints the Sudoku board in a readable format.
    """
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("- - - - - - - - - - - - ")

        for c in range(9):
            if c % 3 == 0 and c != 0:
                print(" | ", end="")

            if c == 8:
                print(board[r][c])
            else:
                print(str(board[r][c]) + " ", end="")


if __name__ == "__main__":
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Unsolved Sudoku:")
    print_board(puzzle)

    if solve_sudoku(puzzle):
        print("\nSolved Sudoku:")
        print_board(puzzle)
    else:
        print("\nNo solution exists for this Sudoku puzzle.")