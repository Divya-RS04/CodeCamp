def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []

    def is_safe(queens, row, col):
        for r in range(row):
            c = queens[r]

            if c == col:
                return False

            if abs(c - col) == abs(r - row):
                return False

        return True

    def dfs(row, queens):
        if row == n:
            solutions.append(queens[:])
            return

        for col in range(n):
            if is_safe(queens, row, col):
                queens.append(col)
                dfs(row + 1, queens)
                queens.pop()

    dfs(0, [])
    return solutions