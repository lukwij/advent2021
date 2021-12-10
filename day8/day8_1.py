# day8_1.py


def get_next_display(filename: str):
    with open(filename) as f:
        for line in f:
            pattern, output = line.split("|")
            pattern = pattern.split()
            output = output.split()
            yield pattern, output


def decode_display(filename: str):
    known_digits = {"1": 0, "4": 0, "7": 0, "8": 0}
    for pattern, output in get_next_display(filename):
        # print(pattern, output)
        for output_digit in output:
            match len(output_digit):
                case 2:
                    known_digits["1"] += 1
                case 4:
                    known_digits["4"] += 1
                case 3:
                    known_digits["7"] += 1
                case 7:
                    known_digits["8"] += 1
    print(known_digits)
    return sum(known_digits.values())


if __name__ == "__main__":
    print(decode_display("input.txt"))
