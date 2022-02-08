def main():
    with open("day7_input.txt") as f:
        positions = [int(x) for x in f.read().strip().split(",")]
        f.close()
        
    positions.sort()
    if len(positions) < 51:
        print(positions)

    mean = round(sum(positions) / len(positions))
    print("mean:", mean)

    sums = []
    # obviously not actually a mean, but I want to quickly see if I have
    # enough computation power to do everything
    #
    # Also not very elegant. But it worked!
    for mean in range(mean - 100, mean + 100):
        if (mean % 10) == 0:
            print("got to", mean)
        diffsum = 0
        for pos in positions:
            if pos > mean:
                a = np.array(range(mean, pos+1)) - mean
            elif pos < mean:
                a = np.array(range(mean, pos-1, -1)) - mean
            else:
                a = np.array([0])
            # print("array for " + str(pos) + ":", a, "(abs sum " + str(abs(sum(a))) + ")")
            diffsum += abs(sum(a))

        # print(diffsum)
        # 101618153 is too high
        # I'm guessing the mean is not necessarily the shortest one
        sums.append(diffsum)
    print("smallest sum:", min(sums))

main()
