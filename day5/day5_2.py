# day5_2.py
from collections import defaultdict


def get_next_vent_line(filename: str):
    with open(filename) as f:
        for line in f:
            start, end = line.split(" -> ")
            x1, y1 = map(int, start.split(","))
            x2, y2 = map(int, end.split(","))
            yield [x1, y1], [x2, y2]


def find_danger_zones(filename: str):
    hydro_vent_map = defaultdict(int)
    for start, end in get_next_vent_line(filename):
        hydro_vent_map[(start[0], start[1])] += 1
        while start != end:
            if start[0] < end[0]:
                start[0] += 1
            elif start[0] > end[0]:
                start[0] -= 1

            if start[1] < end[1]:
                start[1] += 1
            elif start[1] > end[1]:
                start[1] -= 1
            hydro_vent_map[(start[0], start[1])] += 1
    return hydro_vent_map


def count_worst_spots(vent_map):
    worst_spots = 0
    for value in vent_map.values():
        if value > 1:
            worst_spots += 1
    return worst_spots


if __name__ == "__main__":
    v_map = find_danger_zones("input.txt")
    print(count_worst_spots(v_map))
