#!/usr/bin/python3
"""Solves the N queens puzzle.
    N must be an integer >= 4.
    Attributes:
        board (list): A list of lists representing the chessboard
        solutions (list): A list of lists containing solutions
    r and c represent row and column respectively
    """

import sys


def init_board(n):
    """Initialize an N×N chessboard with 0's."""
    board = []
    [board.append([]) for a in range(n)]
    [row.append(' ') for a in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of the chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of lists representation in a board."""
    soln = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                soln.append([r, c])
                break
    return (soln)


def xout(board, row, col):
    """mark spots on a chessboard with "x"."""
    # xout all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"

    # xout all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"

    # xout all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"

    # xout all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"

    # xout all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1

    # xout all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1

    # xout all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

    # xout all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve the N queen peoblem."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            temp_board = board_deepcopy(board)
            temp_board[row][c] = "Q"
            xout(temp_board, row, c)
            solutions = recursive_solve(temp_board, row + 1,
                                        queens + 1, solutions)
    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for soln in solutions:
        print(soln)
