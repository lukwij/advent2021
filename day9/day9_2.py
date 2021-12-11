# day9_2.py
from functools import reduce

from day9_1 import get_positions


def find_low_points(filename: str) -> list[list[tuple[int, int]]]:
    heightmap = get_positions(filename)
    basins = []
    for i, row in enumerate(heightmap):
        for j, height in enumerate(row):
            if 9 == height:
                continue
            adjacent_positions = find_adjacent_positions((i, j), heightmap)
            basin_numbers_of_adjacent = [find_basin_number(adjacent_position, basins) for adjacent_position in adjacent_positions]
            basin_numbers_of_adjacent = sorted(list(set([number for number in basin_numbers_of_adjacent if number is not None])))
            if len(basin_numbers_of_adjacent) == 2:
                basins[basin_numbers_of_adjacent[0]] = basins[basin_numbers_of_adjacent[0]] + basins.pop(basin_numbers_of_adjacent[1])
                basins[basin_numbers_of_adjacent[0]].append((i, j))
            elif len(basin_numbers_of_adjacent) == 1:
                basins[basin_numbers_of_adjacent[0]].append((i, j))
            else:
                basins.append([(i, j)])
            pass
    return basins


def find_3_largest_basins(basins: list[list[tuple[int, int]]]) -> int:
    sorted_by_size = sorted(basins, key=len, reverse=True)
    largest_multiplied = reduce(lambda x, y: x * y, map(len, sorted_by_size[:3]))
    return largest_multiplied


def find_basin_number(position: tuple, basins: list):
    for basin_number, basin in enumerate(basins):
        if position in basin:
            return basin_number


def find_adjacent_positions(position: tuple, heightmap):
    i, j = position
    adjacent_positions = []
    if i > 0:  # check up, exclude first row
        adjacent_positions.append((i - 1, j))
    if j > 0:  # check left, exclude leftmost positions
        adjacent_positions.append((i, j - 1))
    return adjacent_positions


if __name__ == "__main__":
    basins = find_low_points("input.txt")
    print(basins)
    print(find_3_largest_basins(basins))
