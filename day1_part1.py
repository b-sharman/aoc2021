with open("day1_input.txt") as f:
    lines = f.readlines()
    f.close()
    count = 0
    for index, line in enumerate(lines):
        if index == 0: continue
        if int(line.strip()) > int(lines[index - 1].strip()):
            count += 1

    print(count)
