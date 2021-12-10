# day8_2.py


def get_next_display(filename: str):
    with open(filename) as f:
        for line in f:
            pattern, output = line.split("|")
            pattern = pattern.split()
            output = output.split()
            yield pattern, output


def decode_display(filename: str):
    output_sum = 0
    for pattern, output in get_next_display(filename):
        # print(pattern, output)
        translation_map = learn_from_pattern(pattern)
        output_sum += translate_output(output, translation_map)
    return output_sum


def learn_from_pattern(pattern: list[str]) -> dict[int, str]:
    translation_map = {}
    while len(translation_map) < 10:
        for pattern_digit in pattern:
            match len(pattern_digit):
                case 2:
                    translation_map[1] = pattern_digit
                case 4:
                    translation_map[4] = pattern_digit
                case 3:
                    translation_map[7] = pattern_digit
                case 7:
                    translation_map[8] = pattern_digit
                case 5:
                    if 1 in translation_map.keys():
                        if segments_included(translation_map[1], pattern_digit) == 2:
                            translation_map[3] = pattern_digit
                        elif 9 in translation_map.keys():
                            if segments_included(translation_map[9], pattern_digit) == 5:
                                translation_map[5] = pattern_digit
                    if 9 in translation_map.keys():
                        if segments_included(pattern_digit, translation_map[9]) == 4:
                            translation_map[2] = pattern_digit
                case 6:
                    if 1 in translation_map.keys():
                        if segments_included(translation_map[1], pattern_digit) == 1:
                            translation_map[6] = pattern_digit
                    if 4 in translation_map.keys():
                        if segments_included(translation_map[4], pattern_digit) == 4:
                            translation_map[9] = pattern_digit
                    if 5 in translation_map.keys():
                        if segments_included(translation_map[5], pattern_digit) == 4:
                            translation_map[0] = pattern_digit
    return translation_map


def translate_output(output, translation_map) -> int:
    translated_output = []
    for output_digit in output:
        for candidate in [digit for digit in translation_map.values() if len(digit) == len(output_digit)]:
            found = True
            for character in output_digit:
                if character not in candidate:
                    found = False
                    break
            if found:
                index_of_segments = list(translation_map.values()).index(candidate)
                translated_digit = list(translation_map.keys())[index_of_segments]
                translated_output.append(translated_digit)
    return int("".join(map(str, translated_output)))


def segments_included(given, test):
    return sum([1 for letter in given if letter in test])


if __name__ == "__main__":
    print(decode_display("input.txt"))
