def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board, n)
        return True  # Set to False if you want to find *all* solutions
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtrack
    return False

def print_board(board, n):
    print("\nSolution:")
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()

# -------- Main --------
n = int(input("Enter number of queens (4 or 8): "))
board = [[0 for _ in range(n)] for _ in range(n)]

if not solve_n_queens(board, 0, n):
    print("No solution exists")
