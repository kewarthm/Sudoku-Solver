
def sudoku_print(p):
    for i in p:
        print(*i, sep=' ')

def find_empty_cell(p):
    for i in range(9):
        for j in range(9):
            if p[i][j] == 0:
                return [i, j]

    return [-1, -1]

def safe(p, row, col, dig):
    '''
        (list, int, int, int) -> bool

        If value dig is a valid choice of integer for cell (row, col) in the
        sudoku puzzle p then return True. Otherwise return False
    '''

    if dig in p[row][:col] or dig in p[row][col+1:]:
        return False

    for i in range(9):
        if i != col and dig == p[i][col]:
            return False

    for i in range(row - (row % 3), row + 2 - (row % 3) + 1):
        for j in range(col - (col % 3), col + 2 - (col % 3) + 1):
            if i != row and j != col and dig == p[i][j]:
                return False
    return True

def sudoku_solve(p):
    '''
        (list) -> list

        Takes a sudoku puzzle p and returns a completed sudoku puzzle.
        If no solution exists then it will return the original puzzle
    '''

    next = find_empty_cell(p)
    if next == [-1, -1]:
        return p
    for d in range(1, 10):
        if safe(p, next[0], next[1], d):
            p[next[0]][next[1]] = d
            p = sudoku_solve(p)
            if find_empty_cell(p) == [-1, -1]:
                return p
            else:
                p[next[0]][next[1]] = 0
    return p


if __name__ == "__main__":
    puzzle =[
        [0, 6, 0, 3, 0, 0, 8, 0, 4],
        [5, 3, 7, 0, 9, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 6, 3, 0, 7],
        [0, 9, 0, 0, 5, 1, 2, 3, 8],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 1, 3, 6, 2, 0, 0, 4, 0],
        [3, 0, 6, 4, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 6, 0, 5, 2, 3],
        [1, 0, 2, 0, 0, 9, 0, 8, 0]
    ]
    t1 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    sol = sudoku_solve(puzzle)
    s1 = sudoku_solve(t1)
    sudoku_print(sol)
