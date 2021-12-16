# day14_1.py
from collections import Counter


def get_template_and_rules(filename: str) -> (list, dict):
    with open(filename) as f:
        template = ''
        rules = {}
        for line in f:
            if "->" in line:
                rule = list(line.strip().split(" -> "))
                rules[rule[0]] = rule[1]
            else:
                if line.strip():
                    template = list(line.strip())
        return template, rules


def process_polymer(filename: str, steps: int) -> int:
    template, rules = get_template_and_rules(filename)
    for step in range(steps):
        pairs = list(zip(template[::], template[1::]))
        pairs = [pair[0] + pair[1] for pair in pairs]
        new_elements = [rules[pair] for pair in pairs]
        new_template = template + new_elements
        new_template[::2] = template
        new_template[1::2] = new_elements
        template = new_template
    counter = Counter(template)
    return counter.most_common()[0][1] - counter.most_common()[-1][1]


if __name__ == "__main__":
    print(process_polymer("input.txt", steps=10))
