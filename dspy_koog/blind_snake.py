from random import randint, choice

WIDTH = 1000
HEIGHT = 1000
S = WIDTH * HEIGHT

snake_pos = (randint(0, WIDTH), randint(0, HEIGHT))
apple_pos = (randint(0, WIDTH), randint(0, HEIGHT))

win_condition = lambda: snake_pos == apple_pos
n_steps = 0

while not win_condition() and n_steps < 35 * S:
    direction = choice(["right", "up"])
    n_steps += 1
    if direction == "right":
        snake_pos = ((snake_pos[0] + 1) % WIDTH, snake_pos[1])
    else:  # up
        snake_pos = (snake_pos[0], (snake_pos[1] + 1) % HEIGHT)

if win_condition():
    print(f"You won in {n_steps} steps!")
else:
    print("You lost!")
