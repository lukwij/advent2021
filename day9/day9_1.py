# day9_1.py

def get_positions(filename: str) -> list[list[int]]:
    with open(filename) as f:
        heightmap = [list(map(int, line.strip())) for line in f]
        return heightmap


def find_low_points(filename: str) -> int:
    heightmap = get_positions(filename)
    low_points = []
    for i, row in enumerate(heightmap):
        for j, height in enumerate(row):
            adjacent_heights = []
            if i > 0:  # check top, exclude first row
                adjacent_heights.append(heightmap[i - 1][j])
            if i < len(heightmap) - 1:  # check bottom, exclude last row
                adjacent_heights.append(heightmap[i + 1][j])
            if j > 0:  # check left, exclude leftmost positions
                adjacent_heights.append(heightmap[i][j - 1])
            if j < len(row) - 1:  # check right, exclude rightmost positions
                adjacent_heights.append(heightmap[i][j + 1])

            if height < min(adjacent_heights):
                low_points.append(1 + height)
    return sum(low_points)


if __name__ == "__main__":
    print(find_low_points("input.txt"))
