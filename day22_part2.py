import numpy as np

class Instruction(object):
    """ Represents a single instruction from the input file. """

    def __init__(self, ooo, ranges):
        # on or off
        self.ooo = ooo

        # tuples
        def map_range(r):
            """
            Adjust a range to be a range of indices instead of coordinates.

            For example, a -50 needs to be changed to a 0 and a 50 needs to be
            changed to a 100.
            """
            # Python indices don't include the last one
            return (r[0]+50, r[1]+51)

        self.xr, self.yr, self.zr = [map_range(r) for r in ranges]

    def __str__(self):
        return str(self.ooo) + " " + " ".join([str(r) for r in (self.xr, self.yr, self.zr)])

    @staticmethod
    def parse(line):
        """ Return a new Instruction from a line of input. """
        # true for "on", false for "off"
        ooo = line.split()[0] == "on"

        range_strings = line.split()[1].split(",")
        # x, y, z
        ranges = []
        for s in range_strings:
            lower = int(s[s.index("=")+1:s.index("..")])
            upper = int(s[s.index("..")+2:])
            ranges.append((lower, upper))
        return Instruction(ooo, ranges)

def main():
    with open("day22_input.txt") as f:
        instructions = []
        for l in f.read().splitlines():
            inst = Instruction.parse(l)
            # assumes all ranges are in numerical order
            if all([r[0] >= 0 and r[1] <= 101 for r in (inst.xr, inst.yr, inst.zr)]):
                instructions.append(inst)
        f.close()

    # print(instructions[0])
    # exit()

    # tricky because indices will be either 50 or 51 off (not sure yet)
    # this is compensated for in Instruction.__init__
    cubes = np.empty((101, 101, 101), dtype=np.bool_)
    assert np.count_nonzero(cubes) == 0
    for inst in instructions:
        cubes[inst.xr[0]:inst.xr[1], inst.yr[0]:inst.yr[1], inst.zr[0]:inst.zr[1]] = inst.ooo

    print(np.count_nonzero(cubes))

main()
