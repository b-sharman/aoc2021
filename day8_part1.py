import numpy as np

def main():
    with open("day8_input.txt") as f:
        inputs = []
        outputs = []
        for line in f.readlines():
            line = line.strip()
            # note to future self: inputs are what you use to form a key
            # outputs are what you use that key to decode
            inputs.append(line.split("|")[0].strip().split(" "))
            outputs.append(line.split("|")[1].strip().split(" "))
        f.close()

    total = inputs + outputs
    # print(outputs)

    # number of segments that each digit uses
    spd = {0: 6,
           1: 2,
           2: 5,
           3: 5,
           4: 4,
           5: 5,
           6: 6,
           7: 3,
           8: 7,
           9: 6}
    # 1, 4, 7, and 8 are unique
    unique = (1, 4, 7, 8)

    count = 0
    for output in outputs:
        for s in output:
            if len(s) in [spd[u] for u in unique]:
                count += 1
    print(count)

main()
