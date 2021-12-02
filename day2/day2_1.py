# day2_1.py

def get_next_value(filename: str):
    with open(filename) as f:
        for line in f:
            command, value = line.split()
            yield command, int(value)


def calculate_position(filename: str):
    depth = 0
    horizontal_position = 0
    for command, value in get_next_value(filename):
        match command:
            case "forward":
                horizontal_position += value
            case "down":
                depth += value
            case "up":
                depth -= value
    return depth * horizontal_position


if __name__ == "__main__":
    print(calculate_position("input.txt"))
