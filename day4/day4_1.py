# day4_1.py

BOARD_DIMENSION = 5


def get_random_numbers(filename: str) -> list[int]:
    with open(filename) as f:
        for i, line in enumerate(f):
            if 0 == i:
                random_numbers = list(map(int, line.rstrip().split(",")))
                return random_numbers


def get_next_board(filename: str):
    with open(filename) as f:
        cube = []
        for line in f:
            if BOARD_DIMENSION == len(line.split()):
                cube.append(list(map(int, line.split())))
            if BOARD_DIMENSION == len(cube):
                yield cube
                cube = []


def find_winning_bingo_board(filename: str):
    drawn_numbers = get_random_numbers(filename)
    results = []
    for board in get_next_board(filename):
        turn, score = play_bingo(board, drawn_numbers)
        results.append((turn, score))
    return min(results, key=lambda x: x[0])


def play_bingo(board, drawn_numbers):
    for turn, number in enumerate(drawn_numbers):
        new_board = []
        for row in board:
            new_board.append(["-" if item == number else item for item in row])
        board = new_board
        if check_winning_condition(board):
            new_board = []
            for row in board:
                new_board.append([0 if item == "-" else item for item in row])
            board = new_board
            sum_of_unmarked = sum([sum(row) for row in board])
            return turn, number * sum_of_unmarked
    return 1000, 0


def check_winning_condition(board):
    for i in range(BOARD_DIMENSION):
        column = []
        for row in board:
            if set(row) == {"-"}:
                return True
            column.append(row[i])
        if set(column) == {"-"}:
            return True
    return False


if __name__ == "__main__":
    print(find_winning_bingo_board("input.txt"))
