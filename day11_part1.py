import numpy as np

num_flashes = 0

def flash(octopi, row, col):
    """ Modify octopi by incrementing a 3x3 block by 1. """
    global num_flashes

    octopi[max(row-1, 0):row+2, max(col-1, 0):col+2] += 1
    num_flashes += 1

def main():
    global num_flashes

    with open("day11_input.txt") as f:
        octopi = np.array([[int(char) for char in line] for line in f.read().splitlines()])
        f.close()

    print(octopi)

    for i in range(100):
        octopi += 1
        # a single octopi can only flash once per step
        already_flashed = []
        while (octopi > 9).any():
            for row in range(octopi.shape[1]):
                for col in range(octopi.shape[0]):
                    if (octopi[row, col] > 9):
                        if ((row, col) not in already_flashed):
                            # flash
                            flash(octopi, row, col)
                            already_flashed.append((row, col))
                        else:
                            # Keep track of it so it can be reset at the end
                            octopi[row, col] = -1000
        octopi[octopi < 0] = 0 # remove negatives that didn't overflow
        print(f"\nAfter step {i+1}:")
        print(octopi)

    print(num_flashes)

main()
