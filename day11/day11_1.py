# day11_1.py

GRID_ROWS = 10
ROW_LENGTH = 10


def get_octopus_grid(filename: str) -> list[list[int]]:
    with open(filename) as f:
        grid = [list(map(int, line.strip())) for line in f]
        return grid


def process_flashes(filename: str, steps: int) -> int:
    octopus_grid = get_octopus_grid(filename)
    flash_count = 0
    for step in range(steps):
        check_flash = True
        flash_grid = []
        update_grid = []
        while check_flash:
            check_flash = False
            for i, row in enumerate(octopus_grid):
                for j, position in enumerate(row):
                    if (i, j) not in update_grid:
                        increase_energy_by_1(octopus_grid, i, j)
                        update_grid.append((i, j))
                    if octopus_grid[i][j] > 9 and (i, j) not in flash_grid:
                        check_flash = True
                        flash_grid.append((i, j))
                        for adjacent in find_adjacent_positions(i, j):
                            increase_energy_by_1(octopus_grid, adjacent[0], adjacent[1])
        for coordinates in flash_grid:
            octopus_grid[coordinates[0]][coordinates[1]] = 0
            flash_count += 1
        print_octopus_grid(octopus_grid)
    return flash_count


def increase_energy_by_1(grid, row_number, position_in_row):
    grid[row_number][position_in_row] += 1


def find_adjacent_positions(row, position):
    adjacent = []
    if row > 0:  # check up
        adjacent.append([row - 1, position])
        if position > 0:
            adjacent.append([row - 1, position - 1])
        if position < ROW_LENGTH - 1:
            adjacent.append([row - 1, position + 1])
    if row < GRID_ROWS - 1:  # check down
        adjacent.append([row + 1, position])
        if position > 0:
            adjacent.append([row + 1, position - 1])
        if position < ROW_LENGTH - 1:
            adjacent.append([row + 1, position + 1])
    if position > 0:  # check left
        adjacent.append([row, position - 1])
    if position < ROW_LENGTH - 1:  # check right, exclude rightmost positions
        adjacent.append([row, position + 1])
    return adjacent


def print_octopus_grid(grid):
    for row in grid:
        print(row)
    print("\n")


if __name__ == "__main__":
    print(process_flashes("input.txt", steps=100))
