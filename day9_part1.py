import numpy as np

def main():
    with open("day9_input.txt") as f:
        # big = []
        # for line in f.read().strip().split("\n"):
        #     mini = []
        #     for x in line:
        #         mini.append(int(x))
        #     big.append(mini)
        # heightmap = np.array(big)
        heightmap = np.array([[int(x) for x in line] for line in f.read().strip().split("\n")])
        f.close()

    print(heightmap)

    low_points = []
    for i in range(heightmap.shape[0]):
        for j in range(heightmap.shape[1]):
            adjacents = []
            # add each adjacent value, but only after checks that avoid IndexErrors
            # above
            if (i-1) >= 0:
                adjacents.append(heightmap[i-1][j])
            # below
            if (i+1) < heightmap.shape[0]:
                adjacents.append(heightmap[i+1][j])
            # left
            if (j-1) >= 0:
                adjacents.append(heightmap[i][j-1])
            # right
            if (j+1) < heightmap.shape[1]:
                adjacents.append(heightmap[i][j+1])
            # if the current value is lower than any of its adjacent values
            if heightmap[i][j] < min(adjacents):
                print("local min:", heightmap[i][j])
                low_points.append(heightmap[i][j])

    print("sum:", sum(low_points) + len(low_points))
        
main()
