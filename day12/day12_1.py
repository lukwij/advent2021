# day12_1.py
import copy
from string import ascii_lowercase

FOUND_PATHS = []


def get_cave_connections(filename: str) -> dict:
    connections = {}
    with open(filename) as f:
        for line in f:
            cave1, cave2 = line.strip().split("-")
            if cave1 in connections:
                connections[cave1].append(cave2)
            else:
                connections[cave1] = [cave2]

            if cave2 in connections:
                connections[cave2].append(cave1)
            else:
                connections[cave2] = [cave1]
        return connections


def find_paths(filename: str):
    connections = get_cave_connections(filename)
    print(connections)
    find_next_steps(connections, "start", [])
    print(FOUND_PATHS)
    print(list(filter(is_end_at_the_end, FOUND_PATHS)))
    print(len(list(filter(is_end_at_the_end, FOUND_PATHS))))


def find_next_step(connections: dict, path_so_far: list, current_cave: str):
    """ My own first attempt. Wasn't working well, though."""
    for possible_connection in connections[current_cave]:
        if (possible_connection[0] in ascii_lowercase) and (possible_connection in path_so_far):
            continue
        path_so_far = copy.deepcopy(path_so_far)
        path_so_far.append(possible_connection)
        if possible_connection == "end":
            FOUND_PATHS.append(path_so_far)
            return
        find_next_step(connections, path_so_far, possible_connection)


def find_next_steps(connections, current_cave, visited):
    visited.append(current_cave)
    if current_cave != "end":
        for cave in connections[current_cave]:
            if not ((cave[0] in ascii_lowercase) and (cave in visited)):
                find_next_steps(connections, cave, visited.copy())
    FOUND_PATHS.append(visited)


def is_end_at_the_end(path):
    if path[-1] == "end":
        return True
    return False


if __name__ == "__main__":
    print(find_paths("input.txt"))
