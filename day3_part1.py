def main():
    with open("day3_input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        f.close()

        gamma = [0] * len(lines[0])
        epsilon = [0] * len(lines[0])
        for i in range(len(lines[0])):
            num_1 = 0
            for line in lines:
                num_1 += int(line[i])
            if num_1 > len(lines) / 2:
                gamma[i] = 1
            else:
                epsilon[i] = 1

        print("".join([str(g) for g in gamma]))
        print("".join([str(e) for e in epsilon]))

main()
