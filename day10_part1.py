SCORES = {")": 3, "]": 57, "}": 1197, ">": 25137}
EMPTY = ("()", "[]", "{}", "<>")

def main():
    with open("day10_input.txt") as f:
        lines = f.read().splitlines()
        f.close()

    score = 0
    for line in lines:
        # remove empty chunks
        while any([e in line for e in EMPTY]):
            for e in EMPTY:
                print(line)
                line = "".join(line.split(e))
        print(line)
        # now corruptions will show as a closing bracket immediately after
        # a nonmatching opening bracket
        for i, char in enumerate(line):
            if (char in SCORES) and (line[i-1] not in SCORES):
                print("adding", SCORES[char])
                score += SCORES[char]
        print("\n")

    print(score)

main()
