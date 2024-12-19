def minimize_difference(mat, tar):
    matrix = mat
    target = tar
    if not matrix or not matrix[0]:
        return None

    n = len(matrix)
    m = len(matrix[0])

    best_combination = []
    best_diff = float('inf')

    # Helper function to find the best combination recursively
    def find_best_combination(row, current_sum, combination):
        nonlocal best_combination, best_diff

        if row == n:
            diff = abs(current_sum - target)
            if diff < best_diff:
                best_combination = combination[:]
                best_diff = diff
            return

        for col in range(m):
            new_sum = current_sum + matrix[row][col]
            new_combination = combination + [matrix[row][col]]
            find_best_combination(row + 1, new_sum, new_combination)

    find_best_combination(0, 0, [])

    return best_combination

print( minimize_difference([[1, 2, 3], [3, 4, 5]] , 3 ) )