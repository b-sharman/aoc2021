with open("day1_input.txt") as f:
    lines = f.readlines()
    f.close()
    count = 0
    prev_window_sum = None
    for index, line in enumerate(lines):
        if index < 2: continue
        window_sum = int(line.strip()) + int(lines[index - 1].strip()) + int(lines[index - 2].strip())
        if (prev_window_sum is not None) and (window_sum > prev_window_sum):
            count += 1

        prev_window_sum = window_sum

    print(count) # 1427 is too small
