# -*- coding: utf-8 -*-
"""n_queens.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1r6Tu1-dcLO8IuXA8yQ_4aPAsKUlT8DRW
"""

def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):

    for i in range(row):
        if board[i][col]:
            return False


    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False


    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True


def solve_nqueens_util(board, row, n):
    if row == n:
        print_solution(board)
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = True
            res = solve_nqueens_util(board, row + 1, n) or res
            board[row][col] = False

    return res


def solve_nqueens(n):
    board = [[False for _ in range(n)] for _ in range(n)]
    if not solve_nqueens_util(board, 0, n):
        print("No solution exists.")
    else:
        print("Solutions found.")


n = 3
solve_nqueens(n)

