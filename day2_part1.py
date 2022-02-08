with open("day2_input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    f.close()
    horizontal = 0
    depth = 0
    for index, line in enumerate(lines):
        if line.split()[0] == "forward":
            horizontal += int(line.split()[-1])
        if line.split()[0] == "down":
            depth += int(line.split()[-1])
        if line.split()[0] == "up":
            depth -= int(line.split()[-1])

    print(horizontal, depth, horizontal*depth)
