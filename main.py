# ==========================================================
#  Sudoku Solver - Backtracking Algorithm in Python
#  Repository: https://github.com/Behdad-kanaani/Sudoku-Solver-Python-Backtracking
# ==========================================================

def parse_board(board):
    """
    Preprocess the board to initialize helper data structures:
    - rows, cols, boxes: sets to track used numbers
    - empty: list of empty cells to fill
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty = []

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == ".":
                empty.append((i, j))
            else:
                rows[i].add(num)
                cols[j].add(num)
                box_index = (i // 3) * 3 + (j // 3)
                boxes[box_index].add(num)

    return rows, cols, boxes, empty


def solve_sudoku(board):
    """
    Solves a 9x9 Sudoku puzzle in-place using backtracking.
    """
    rows, cols, boxes, empty = parse_board(board)

    def backtrack(index):
        # If all empty cells are filled, the puzzle is solved
        if index == len(empty):
            return True

        i, j = empty[index]
        box_index = (i // 3) * 3 + (j // 3)

        for digit in map(str, range(1, 10)):
            # Check if the digit is valid in this position
            if digit not in rows[i] and digit not in cols[j] and digit not in boxes[box_index]:
                # Place the digit
                board[i][j] = digit
                rows[i].add(digit)
                cols[j].add(digit)
                boxes[box_index].add(digit)

                # Recursively try to fill in the next cell
                if backtrack(index + 1):
                    return True

                # Backtrack: remove the digit and try the next one
                board[i][j] = "."
                rows[i].remove(digit)
                cols[j].remove(digit)
                boxes[box_index].remove(digit)

        # No valid digit found, need to backtrack
        return False

    backtrack(0)


def print_board(board):
    """
    Nicely print the Sudoku board with grid formatting.
    """
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(val, end=" ")
        print()


if __name__ == "__main__":
    # Sample 9x9 Sudoku board with empty cells as "."
    sudoku_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    print("🔢 Initial Sudoku Board:\n")
    print_board(sudoku_board)

    solve_sudoku(sudoku_board)

    print("\n✅ Solved Sudoku Board:\n")
    print_board(sudoku_board)
