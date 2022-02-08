PAIRS = str.maketrans({"(": ")", "[": "]", "{": "}", "<": ">"})
SCORES = {")]}>"[i]: i+1 for i in range(4)}
EMPTY = ("()", "[]", "{}", "<>")

def main():
    with open("day10_input.txt") as f:
        lines = f.read().splitlines()
        f.close()

    modified = []
    for line in lines:
        # remove empty chunks
        while any([e in line for e in EMPTY]):
            for e in EMPTY:
                print(line)
                line = "".join(line.split(e))
        print(line)
        # now corruptions will show as a closing bracket immediately after
        # a nonmatching opening bracket
        corrupt = False
        for i, char in enumerate(line):
            if (char in SCORES) and (line[i-1] not in SCORES):
                corrupt = True
        if not corrupt:
            modified.append(line)
        print("\n")
    print("modified:", modified)

    # s[::-1] reverses the string; .translate(PAIRS) changes opening
    # chars to closing chars
    closings = [s[::-1].translate(PAIRS) for s in modified]
    scores = []
    for c in closings:
        score = 0
        for char in c:
            score = (score*5) + SCORES[char]
        scores.append(score)
    scores.sort()
    print(scores[len(scores)//2])

main()
