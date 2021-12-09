# day7_1.py


def get_positions(filename: str) -> list[int]:
    with open(filename) as f:
        for line in f:
            positions = list(map(int, line.split(",")))
            return positions


def find_total_fuel_consumption(filename: str):
    positions = get_positions(filename)
    fuel_consumption = []
    for position in positions:
        test_position_list = [position] * len(positions)
        fuel_consumption.append(sum(list(map(count_fuel_consumption, test_position_list, positions))))
    return min(fuel_consumption)


def count_fuel_consumption(test_position, position):
    return abs(test_position - position)


if __name__ == "__main__":
    print(find_total_fuel_consumption("input.txt"))
