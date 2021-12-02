# day2_1.py

def get_next_value(filename: str):
    with open(filename) as f:
        for line in f:
            yield int(line)


def count_uptake(filename: str):
    uptake = 0
    old_value = None
    for value in get_next_value(filename):
        if old_value:
            if value > old_value:
                uptake += 1
        old_value = value
    return uptake


if __name__ == "__main__":
    print(count_uptake("input.txt"))
