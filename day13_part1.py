import numpy as np

# I think there are prettier ways of doing this, but this works
translate = np.vectorize({False: ".", True: "#"}.__getitem__)

def pretty_print(paper):
    # swapaxes because arrays are indexed in row-major order, but
    # the code uses the form paper[x, y]
    for row in np.swapaxes(translate(paper), 0, 1):
        print("".join(row))
    print()

def initialize():
    """ Parse the input file and return the paper as an array and the instructions as a list of tuples. """
    with open("day13_input_small.txt") as f:
        # if only readlines removed the newlines!
        lines = f.read().splitlines()
        f.close()

    # populate lists of coordinates
    # they are split into two lists to facilitate array indexing
    xcoords = []
    ycoords = []
    for line in lines[:lines.index("")]:
        s = line.split(",")
        xcoords.append(int(s[0]))
        ycoords.append(int(s[1]))

    # populate a list of instructions
    instructions = []
    for l in lines[lines.index("")+1:]:
        s = l.split("=")
        instructions.append((s[0][-1], int(s[-1])))

    # none of the coordinates are negative
    # the +1 is because indices start at 0
    paper = np.zeros((max(xcoords)+1, max(ycoords)+1), dtype=bool)
    print("paper.shape", paper.shape)
    # with numpy, we only need one loopless line to make the paper
    paper[np.array(xcoords), np.array(ycoords)] = True

    return paper, instructions

def fold(paper, line):
    """ Folds a new paper given a line tuple (axis, value).  """
    # | is the bitwise or
    ret = paper.copy()
    if line[0] == "x":
        # we have to fold the bottom part up
        # if the bottom is bigger, add Falses to the top so they are the same size
        # if the top is bigger, only modify the bottom part of the top that is the
        #   the same size as the bottom
        
        # if bottom is less than or equal to top, no added Falses are necessary
        if (paper.shape[1] - line[1]) <= (line[1] - 1):
            ret[(2*line[1]) - ret.shape[1] - 1:line[1]] |= np.flipud(ret[line[1]+1:])
        # if the bottom is greater than the top
        else:
            # start with the bottom
            ret = np.flipud(ret[line[1]+1:])
            # now add the top
            ret[ret.shape[1] - line[1] - 1:] |= paper[:line[1]]
    elif line[0] == "y":
        # if the left is greater than or equal to the right, we have to do fancy shmancy indexing
        if (line[1] - 1) >= (paper.shape[0] - line[1]):
            print("ret")
            pretty_print(ret)
            print("ret[:, (2*line[1]) - paper.shape[0]:line[1]]")
            pretty_print(ret[:, (2*line[1]) - paper.shape[0]:line[1]])
            print("np.fliplr(ret[:, line[1]+1:])")
            pretty_print(np.fliplr(ret[:, line[1]+1:]))
            ret[:, (2*line[1]) - paper.shape[0]:line[1]] |= np.fliplr(ret[:, line[1]+1:])
        # if the right is greater than the left, we just reverse the right and put
        #   the left on top of it
        else:
            # start with the right
            ret = np.fliplr(ret[:, line[1]+1:])
            # now add the left
            ret[:, ret.shape[0] - line[1] - 1:] |= paper[:, :line[1]]
    return ret

def main():
    paper, instructions = initialize() # 2D np array
    pretty_print(paper)

    first_fold = True
    for instruction in instructions:
        paper = fold(paper, instruction)
        pretty_print(paper)
        if first_fold:
            print(f"after first fold: {np.count_nonzero(paper)} dots")
            first_fold = False

    print(f"end with {np.count_nonzero(paper)} dots")

main()
