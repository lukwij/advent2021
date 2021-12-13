# day13_2.py
from day13_1 import get_dot_grid_and_folds


def process_folds(filename: str) -> int:
    grid, folds = get_dot_grid_and_folds(filename)
    for fold in folds:
        fold_type = fold[0]
        fold_position = int(fold[1])
        temporary_table = []
        for i, dot in enumerate(grid):
            if "x" == fold_type:
                if dot[0] < fold_position:
                    temporary_table.append(dot)
                elif dot[0] > fold_position:
                    temporary_table.append([2 * fold_position - dot[0], dot[1]])
            if "y" == fold_type:
                if dot[1] < fold_position:
                    temporary_table.append(dot)
                elif dot[1] > fold_position:
                    temporary_table.append([dot[0], 2 * fold_position - dot[1]])
        grid = temporary_table
    grid = set(map(tuple, grid))
    draw_grid(grid)
    return len(grid)


def draw_grid(grid):
    max_x, max_y = max([(x, y) for x, y in grid])
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x,y) in list(grid):
                print("#", end="")
            else:
                print(".", end="")
        print("")


if __name__ == "__main__":
    process_folds("input.txt")
