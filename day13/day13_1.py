# day13_1.py


def get_dot_grid_and_folds(filename: str):
    with open(filename) as f:
        grid = []
        folds = []
        for line in f:
            if "," in line:
                grid.append(list(map(int, line.strip().split(","))))
            if "=" in line:
                instruction = line.split()[2]
                folds.append(instruction.split("="))
        return grid, folds


def process_folds(filename: str, max_folds: int) -> int:
    grid, folds = get_dot_grid_and_folds(filename)
    for fold_number, fold in enumerate(folds):
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
        if max_folds == fold_number + 1:
            break
    grid = set(map(tuple, grid))

    return len(grid)


if __name__ == "__main__":
    print(process_folds("input.txt", max_folds=1))
