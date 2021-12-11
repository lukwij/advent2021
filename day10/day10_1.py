# day10_1.py

def get_navigation_subsystem_copy(filename: str) -> list[str]:
    with open(filename) as f:
        navigation = [line.strip() for line in f]
        return navigation


def find_error_characters(filename: str) -> list[str]:
    navigation = get_navigation_subsystem_copy(filename)
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    error_characters = []
    for line in navigation:
        openings = []
        for character in line:
            if character in pairs.keys():
                openings.append(character)
            else:
                if openings[-1] == list(pairs.keys())[list(pairs.values()).index(character)]:
                    openings.pop()
                else:
                    error_characters.append(character)
                    break
    print(error_characters)
    return error_characters


def find_error_score(error_characters):
    char_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = sum([char_score[char] for char in error_characters])
    return score


if __name__ == "__main__":
    errors = find_error_characters("input.txt")
    print(find_error_score(errors))
