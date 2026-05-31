def dfs(matrix, node):
    visited = []
    stack = [node]

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.append(current)

            for neighbor in range(len(matrix[current]) - 1, -1, -1):
                if matrix[current][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)

    return visited