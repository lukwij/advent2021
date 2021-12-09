# day7_2.py
import sys

from day7_1 import get_positions

sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())


def find_total_fuel_consumption(filename: str):
    positions = get_positions(filename)
    fuel_consumption = []
    for test_position in range(max(positions)):
        test_position_list = [test_position] * len(positions)
        print(test_position_list, positions)
        fuel_consumption.append(sum(list(map(count_fuel_consumption, test_position_list, positions))))
    print(fuel_consumption)
    return min(fuel_consumption)


def count_fuel_consumption(test_position, position):
    return recursive_fuel(abs(test_position - position))


def recursive_fuel(move: int) -> int:
    if move == 0:
        return 0
    else:
        return move + recursive_fuel(move - 1)


if __name__ == "__main__":
    print(find_total_fuel_consumption("input.txt"))
