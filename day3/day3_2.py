# day3_2.py
import copy

from day3.day3_1 import get_values, convert_list_to_dec


def calculate_life_support(filename: str):
    values_oxygen = get_values(filename)
    values_co2 = copy.deepcopy(values_oxygen)
    for bit_position in range(len(values_oxygen[0])):
        ones_count_in_oxygen = sum([int(value[bit_position]) for value in values_oxygen])
        ones_count_in_co2 = sum([int(value[bit_position]) for value in values_co2])
        if ones_count_in_oxygen >= len(values_oxygen) / 2:
            found_oxygen_bit = "1"
        else:
            found_oxygen_bit = "0"

        if ones_count_in_co2 < len(values_co2) / 2:
            found_co2_bit = "1"
        else:
            found_co2_bit = "0"
        if len(values_oxygen) > 1:
            values_oxygen = list(filter(lambda x: x[bit_position] == found_oxygen_bit, values_oxygen))
        if len(values_co2) > 1:
            values_co2 = list(filter(lambda x: x[bit_position] == found_co2_bit, values_co2))
        pass

    oxygen_gen_dec = convert_list_to_dec(values_oxygen)
    co2_scrubber_dec = convert_list_to_dec(values_co2)
    return oxygen_gen_dec * co2_scrubber_dec


if __name__ == "__main__":
    print(calculate_life_support("input.txt"))
