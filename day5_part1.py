"""
Psuedocode

parse the input into line objects
find the most extreme values
make a grid big enough to hold all the lines
for each line,
    increment each spot on the grid that holds that line
count the number of locations on the grid holding 2 or greater
"""

import numpy as np

class Line(object):
    """ An object representing a line """

    def __init__(self, coord0, coord1):
        """ Coords are tuples (x, y). """
        self.x0, self.y0 = coord0
        self.x1, self.y1 = coord1

        if self.x0 == self.x1:
            self.orientation = "vertical"
            # order coordinates from smallest to largest
            self.y0, self.y1 = sorted((coord0[1], coord1[1]))
        elif self.y0 == self.y1:
            self.orientation = "horizontal"
            # order coordinates from smallest to largest
            self.x0, self.x1 = sorted((coord0[0], coord1[0]))
        elif coord0 == coord1: # shouldn't happen
            self.orientation = None
        else:
            self.orientation = "diagonal"

    def __str__(self):
        return "(" + str(self.x0) + ", " + str(self.y0) + ") to (" + str(self.x1) + ", " + str(self.y1) + ")"

    @staticmethod
    def line_from_string(string):
        """ Return a line object from a string in form "x0,y0 -> x1,y1" """
        coord0, coord1 = string.split(" -> ")
        def change(coord):
            return tuple([int(x) for x in coord.split(",")])
        coord0 = change(coord0)
        coord1 = change(coord1)
        return Line(coord0, coord1)


def main():
    with open("day5_input.txt") as f:
        strings = [line.strip() for line in f.readlines()]
        f.close()
        
        lines = [Line.line_from_string(s) for s in strings]

        greatest_x = max([l.x1 for l in lines])
        greatest_y = max([l.y1 for l in lines])
        grid = np.zeros((greatest_y + 1, greatest_x + 1), dtype=np.intp)

        # apply all lines
        for line in lines:
            # print(line)
            if line.orientation == "horizontal":
                grid[line.y0, line.x0:line.x1+1] += 1
            elif line.orientation == "vertical":
                grid[line.y0:line.y1+1, line.x0] += 1

        if grid.shape[1] < 16:
            print(grid)
        print("Number of 2 or more:", np.count_nonzero(grid >= 2))

main()
