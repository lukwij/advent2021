# day10_2.py
from math import floor


def get_navigation_subsystem_copy(filename: str) -> list[str]:
    with open(filename) as f:
        navigation = [line.strip() for line in f]
        return navigation


def find_completion_sequences(filename: str) -> list[list[str]]:
    navigation = get_navigation_subsystem_copy(filename)
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    closing_sequences = []
    for line in navigation:
        openings = []
        for character in line:
            if character in pairs.keys():
                openings.append(character)
            else:
                if openings[-1] == list(pairs.keys())[list(pairs.values()).index(character)]:
                    openings.pop()
                else:
                    openings = []
                    break
        if openings:
            closing_sequences.append([pairs[opening] for opening in openings[::-1]])
    print(closing_sequences)
    return closing_sequences


def find_completion_score(sequences):
    char_score = {")": 1, "]": 2, "}": 3, ">": 4}
    sequence_scores = []
    for sequence in sequences:
        sequence_score = 0
        for character in sequence:
            sequence_score = (sequence_score * 5) + char_score[character]
        sequence_scores.append(sequence_score)
    score = sorted(sequence_scores)[int(floor(len(sequence_scores) / 2))]
    return score


if __name__ == "__main__":
    completion_sequences = find_completion_sequences("input.txt")
    print(find_completion_score(completion_sequences))
