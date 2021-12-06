# day3_1.py

def get_values(filename: str):
    with open(filename) as f:
        values = [line.strip() for line in f]
    return values


def calculate_power_consumption(filename: str):
    values = get_values(filename)
    entries_count = len(values)
    gamma_rate = [0] * 12
    for value in values:
        for i, bit in enumerate(value):
            gamma_rate[i] += int(bit)
    for i, count in enumerate(gamma_rate):
        if gamma_rate[i] > entries_count / 2:
            gamma_rate[i] = 1
        elif gamma_rate[i] == entries_count / 2:
            raise Exception
        else:
            gamma_rate[i] = 0
    epsilon_rate = [int(not bit) for bit in gamma_rate]

    gamma_rate_dec = convert_list_to_dec(gamma_rate)
    epsilon_rate_dec = convert_list_to_dec(epsilon_rate)

    return gamma_rate_dec * epsilon_rate_dec


def convert_list_to_dec(input_list: list[int]) -> int:
    bin_str = ''.join([str(bit) for bit in input_list])
    integer = int(bin_str, 2)
    return integer


if __name__ == "__main__":
    print(calculate_power_consumption("input.txt"))
