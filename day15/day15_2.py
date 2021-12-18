# day15_2.py
from day15_1 import get_adjacencies, dijkstra


def get_risk_levels(filename: str):
    risk_levels = []
    with open(filename) as f:
        for y, line in enumerate(f):
            risk_levels.append(list(map(int, line.strip())))
    return risk_levels


def find_safe_path(filename: str):
    risk_level_map = get_risk_levels(filename)
    risk_level_map = expand_map(risk_level_map, 5, 5)
    add_positions_to_map(risk_level_map)
    adj = get_adjacencies(risk_level_map)
    target = (len(risk_level_map) - 1, len(risk_level_map[0]) - 1)
    parent, d = dijkstra(adj, (0, 0), target)
    print(f"parent: {parent}\nd: {d}")
    return d[target]


def expand_map(ex_map, mult_x, mult_y) -> list:
    dimension_x = len(ex_map[0])
    dimension_y = len(ex_map)

    for i in range(len(ex_map)):
        for j in range(mult_x - 1):
            ex_map[i] += (list(map(cycle_value_to_9, ex_map[i][-dimension_x:])))

    for i in range(len(ex_map) * (mult_y - 1)):
        ex_map.append(list(map(cycle_value_to_9, ex_map[-dimension_y])))
    return ex_map


def add_positions_to_map(rmap):
    for y, row in enumerate(rmap):
        for x, risk in enumerate(row):
            rmap[y][x] = ((y, x), risk)


def cycle_value_to_9(value):
    if value < 9:
        return value + 1
    else:
        return 1


if __name__ == "__main__":
    print(find_safe_path("input.txt"))
