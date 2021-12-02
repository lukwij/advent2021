# day1_2.py
import time

from day1.day1_1 import get_next_value


def count_sliding_sum_uptake(filename: str):
    uptake = 0
    previous_sum = None
    window = []

    for value in get_next_value(filename):
        window.append(value)
        if 3 == len(window):
            current_sum = sum(window)
            if previous_sum:
                if current_sum > previous_sum:
                    uptake += 1
            previous_sum = current_sum
            window.pop(0)
    return uptake


if __name__ == "__main__":
    start = time.perf_counter()
    print(count_sliding_sum_uptake("input.txt"))
    end = time.perf_counter()
    print(f"Elapsed time: {end - start}s")
