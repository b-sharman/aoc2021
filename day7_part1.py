"""
Psuedocode

"""

def main():
    with open("day7_input.txt") as f:
        positions = [int(x) for x in f.read().strip().split(",")]
        f.close()
        
    positions.sort()
    print("positions:", positions)

    if len(positions) % 2 == 0:
        med = (positions[len(positions) // 2] + positions[(len(positions) // 2) - 1]) / 2
    else:
        med = positions[len(positions) // 2]
    print("median:", med)

    distances = 0
    for pos in positions:
        distances += abs(pos - med)
    print("distances:", distances)

main()
