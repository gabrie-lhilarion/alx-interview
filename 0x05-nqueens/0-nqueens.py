#!/usr/bin/python3
"""
N Queens Puzzle Solver
This script solves the N queens puzzle for a given N.
Usage: nqueens N
"""

import sys


def print_solutions(solutions):
    """Prints all solutions in the specified format"""
    for solution in solutions:
        print(solution)


def is_safe(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col, solutions):
    """Solves the N queens puzzle using backtracking"""
    if col >= len(board):
        solution = [[i, board[i].index(1)] for i in range(len(board))]
        solutions.append(solution)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, solutions) or res
            board[i][col] = 0
    return res


def nqueens(N):
    """Main function to solve the N queens puzzle"""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    print_solutions(solutions)


def main():
    """Main entry point of the script"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)


if __name__ == "__main__":
    main()
