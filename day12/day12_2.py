# day12_2.py
from day12_1 import get_cave_connections, is_end_at_the_end
from string import ascii_lowercase

FOUND_PATHS = []


def find_paths(filename: str):
    connections = get_cave_connections(filename)
    find_next_steps(connections, "start", [])
    print(list(filter(is_end_at_the_end, FOUND_PATHS)))
    print(len(list(filter(is_end_at_the_end, FOUND_PATHS))))


def find_next_steps(connections, current_cave, visited):
    visited.append(current_cave)
    if current_cave != "end":
        for cave in connections[current_cave]:
            if cave != "start":
                if not (is_small_cave(cave) and cave in visited and small_cave_visited_twice(visited)):
                    find_next_steps(connections, cave, visited.copy())
    FOUND_PATHS.append(visited)


def small_cave_visited_twice(path):
    for cave in path:
        if is_small_cave(cave):
            if path.count(cave) == 2:
                return True
    return False


def is_small_cave(cave):
    if cave[0] in ascii_lowercase:
        return True
    return False


if __name__ == "__main__":
    find_paths("input.txt")
