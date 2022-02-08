import numpy as np

def main():
    with open("day9_input_small.txt") as f:
        # The following list comprehension condenses these lines:
        # big = []
        # for line in f.read().splitlines():
        #     mini = []
        #     for x in line:
        #         mini.append(int(x))
        #     big.append(mini)
        # heightmap = np.array(big)
        heightmap = np.array([[int(x) for x in line] for line in f.read().splitlines()])
        f.close()
    print(heightmap)

main()
