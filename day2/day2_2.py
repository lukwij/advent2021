# day2_2.py

from day2.day2_1 import get_next_value


def calculate_position(filename: str):
    aim = 0
    horizontal_position = 0
    depth = 0
    for command, value in get_next_value(filename):
        match command:
            case "forward":
                horizontal_position += value
                depth += value * aim
            case "down":
                aim += value
            case "up":
                aim -= value
    return depth * horizontal_position


if __name__ == "__main__":
    print(calculate_position("input.txt"))
