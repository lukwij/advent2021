# day17_2.py
import re

DRAG = 1
GRAVITY = 1
START = (0, 0)


def get_input(filename: str):
    with open(filename) as f:
        return list(map(int, re.findall(r'-?\d+', f.readline().strip())))


def probe_launching_trials(filename):
    target = x_min, x_max, y_min, y_max = get_input(filename)
    initial_x_velocity = 0
    initial_y_velocity = -200
    successful_trials = []
    while True:
        initial_x_velocity += 1
        result = launch_probe(initial_x_velocity, initial_y_velocity, target)
        if result[0]:
            successful_trials.append((initial_x_velocity, initial_y_velocity))
        elif 1 == result[1] and is_too_far(result[2][0], x_max):
            initial_x_velocity = 0
            initial_y_velocity += 1
            if initial_y_velocity > 200:
                break
    return len(successful_trials)


def launch_probe(velocity_x, velocity_y, target):
    current_position = list(START)
    step = 0
    success = False
    while not is_overshot(current_position, target):
        step += 1
        current_position[0] += velocity_x
        current_position[1] += velocity_y
        velocity_x, velocity_y = adjust_velocity_for_gravity_and_drag(velocity_x, velocity_y)
        if target_hit(current_position, target):
            success = True
            break
    return success, step, current_position


def is_overshot(position, target) -> bool:
    if is_too_far(position[0], target[1]) or is_too_low(position[1], target[2]):
        return True
    return False


def adjust_velocity_for_gravity_and_drag(velocity_x, velocity_y):
    if velocity_x > 0:
        velocity_x -= 1
    elif velocity_x < 0:
        velocity_x += 1

    velocity_y -= 1

    return velocity_x, velocity_y


def target_hit(position, target) -> bool:
    if (target[0] <= position[0] <= target[1]) and (target[2] <= position[1] <= target[3]):
        return True
    return False


def is_too_far(current_x_position, max_x):
    if current_x_position > max_x:
        return True
    return False


def is_too_low(current_y_position, min_y):
    if current_y_position < min_y:
        return True
    return False


if __name__ == "__main__":
    successful_init_velocities = probe_launching_trials("input.txt")
    print(successful_init_velocities)
