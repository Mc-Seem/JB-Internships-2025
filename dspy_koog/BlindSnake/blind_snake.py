from random import randint, choice
import argparse
import sys


def main(width: int, height: int) -> int:
    S = width * height
    if S > 1_000_000:
        print("Error: S = width * height must be lower than 1000000.", file=sys.stderr)
        return 1

    snake_pos = (randint(0, width - 1), randint(0, height - 1))
    apple_pos = (randint(0, width - 1), randint(0, height - 1))

    win_condition = lambda: snake_pos == apple_pos
    n_steps = 0

    while not win_condition() and n_steps < 35 * S:
        direction = choice(["right", "up"])
        n_steps += 1
        if direction == "right":
            snake_pos = ((snake_pos[0] + 1) % width, snake_pos[1])
        else:  # up
            snake_pos = (snake_pos[0], (snake_pos[1] + 1) % height)

    if win_condition():
        print(f"You won in {n_steps} steps!")
    else:
        print("You lost!")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Blind snake simulation. Provide width and height.")
    parser.add_argument("width", type=int, help="Board width (positive integer)")
    parser.add_argument("height", type=int, help="Board height (positive integer)")
    args = parser.parse_args()

    if args.width <= 0 or args.height <= 0:
        print("Error: width and height must be positive integers.", file=sys.stderr)
        sys.exit(1)

    sys.exit(main(args.width, args.height))
