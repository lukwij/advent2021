# day4_2.py
from day4.day4_1 import get_next_board, get_random_numbers, play_bingo


def find_winning_bingo_board(filename: str):
    drawn_numbers = get_random_numbers(filename)
    results = []
    for board in get_next_board(filename):
        turn, score = play_bingo(board, drawn_numbers)
        results.append((turn, score))
    return max(results, key=lambda x: x[0])


if __name__ == "__main__":
    print(find_winning_bingo_board("input.txt"))
