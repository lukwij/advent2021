# day6_1_2.py


def get_fish(filename: str) -> list[int]:
    with open(filename) as f:
        for line in f:
            fish_school = list(map(int, line.split(",")))
            return fish_school


def subtract_or_turn_to_6(value):
    if 0 == value:
        value = 6
    else:
        value -= 1
    return value


def count_fish_on_given_day_map(filename: str, days: int) -> int:
    fish_school = get_fish(filename)
    for day in range(days):
        to_add = fish_school.count(0)
        fish_school = list(map(subtract_or_turn_to_6, fish_school))
        fish_school += [8] * to_add
        print(f"day: {day + 1}: {len(fish_school)}")
    return len(fish_school)


def count_fish_on_given_day_trick(filename: str, days: int) -> int:
    fish_school = get_fish(filename)
    fish_life = []
    for i in range(7):
        fish_life.append([fish_school.count(i), 0])
    for day in range(days):
        fish_life[(day + 2) % 7][1] = fish_life[day % 7][0]
        fish_life[day % 7][0] += fish_life[day % 7][1]
        fish_life[day % 7][1] = 0
        print(f"day: {day + 1}: {fish_life}")
        pass
    return sum(list(map(sum,fish_life)))


if __name__ == "__main__":
    # print(count_fish_on_given_day_map("test.txt", days=80))
    print(count_fish_on_given_day_trick("input.txt", days=256))
