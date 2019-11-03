def within_bound(matrix, row, col):
    row_idx_limit, col_idx_limit = len(matrix), len(matrix[0])
    return 0 <= row < row_idx_limit and 0 <= col < col_idx_limit

def get_next_direction(direction):

    if direction is 'UP':
        return 'LEFT'
    if direction is 'LEFT':
        return 'DOWN'
    if direction is 'DOWN':
        return 'RIGHT'
    return 'UP'

def get_next_coordinates(direction, row, col):

    if direction is 'UP':
        return row - 1, col
    if direction is 'LEFT':
        return row, col - 1
    if direction is 'DOWN':
        return row + 1, col
    return row, col + 1


def get_spiral_path(matrix, row, col):

    matrix_size = len(matrix) * len(matrix[0])
    path = [matrix[row][col]]
    direction = 'UP'  # init direction, changable.
    direction_move = 0  # count the direction move.
    count_step = 1  # for marking the steps needed on each direction.

    while len(path) < matrix_size:
        # increment the count_step in every 2 direction move.
        if(direction_move == 2):
            direction_move = 0
            count_step += 1
        for _ in range(count_step):
            row, col = get_next_coordinates(direction, row, col)
            if within_bound(matrix, row, col):
                path.append(matrix[row][col])
        direction_move += 1
        direction = get_next_direction(direction)
    return path

arr = [
    [13, 12, 11, 10, 25],
    [14, 3, 2, 9, 24],
    [15, 4, 1, 8, 23],
    [16, 5, 6, 7, 22],
    [17, 18, 19, 20, 21]
]

print(get_spiral_path(arr, 2, 1))