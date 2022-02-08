def binary_to_decimal(num):
    num = str(num)
    output = 0
    for i, digit in enumerate(num):
        output += int(digit) * 2 ** (len(num) - i - 1)
    return output

def find_rating(iterable, co=False):
        index = 0
        while len(iterable) > 1:
            # bits at the current index
            bits = [n[index] for n in iterable]
            to_keep = bits.count("1") >= len(bits)/2
            if co:
                to_keep = not to_keep
            # int converts bool to 1 or 0, then str converts that to a str
            to_keep = str(int(to_keep))
            # remove numbers whose bit at index is not the one to keep
            iterable = list(filter(lambda n: n[index] == to_keep, iterable))
            # next iteration, scan the next bit
            index += 1

        return int(iterable[0])

def main():
    with open("day3_input.txt") as f:
        lines = [line.strip() for line in f.readlines()]
        f.close()

        oxygen = find_rating(lines.copy())
        co2 = find_rating(lines.copy(), True)

        print(oxygen, binary_to_decimal(oxygen))
        print(co2, binary_to_decimal(co2))
        print(binary_to_decimal(oxygen) * binary_to_decimal(co2))

main()
