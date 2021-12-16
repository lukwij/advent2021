# day14_2.py
from day14_1 import get_template_and_rules


def process_polymer(filename: str, steps: int) -> int:
    template, rules = get_template_and_rules(filename)
    last_letter = template[-1]
    pairs_counter = initialize_pairs_counter(template, rules)
    for step in range(steps):
        step_increase = dict.fromkeys(pairs_counter.keys(), 0)
        for pair in pairs_counter:
            pair_initial_count = pairs_counter[pair]
            step_increase[pair[0] + rules[pair]] += pair_initial_count
            step_increase[rules[pair] + pair[1]] += pair_initial_count
        pairs_counter = step_increase

    letter_counter = {}
    for pair in pairs_counter:
        if pair[0] in letter_counter:
            letter_counter[pair[0]] += pairs_counter[pair]
        else:
            letter_counter[pair[0]] = pairs_counter[pair]
    letter_counter[last_letter] += 1
    letter_counter = sorted(letter_counter.items(), key=lambda item: item[1])
    return letter_counter[-1][1] - letter_counter[0][1]


def initialize_pairs_counter(template, rules):
    pairs_counter = dict.fromkeys(rules.keys(), 0)
    pairs = zip(template[::], template[1::])
    pairs = [pair[0] + pair[1] for pair in pairs]
    for pair in pairs:
        pairs_counter[pair] += 1
    return pairs_counter


if __name__ == "__main__":
    print(process_polymer("input.txt", steps=40))
