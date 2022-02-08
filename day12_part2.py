class Connection(object):
    """ Container holding two linked caves that, when indexed by one, returns the other. """

    def __init__(self, a, b):
        self.a, self.b = a, b

    def __contains__(self, item):
        # item in (self.a, self.b) is shorter, but I think this may be faster?
        return (item == self.a) or (item == self.b)

    def __getitem__(self, i):
        if i == self.a:
            return self.b
        elif i == self.b:
            return self.a
        else:
            raise IndexError("index for " + str(self) + " must either be " + self.a + " or " + self.b)

    def __str__(self):
        return self.a + "-" + self.b

    def __repr__(self):
        return str(self)

    @staticmethod
    def parse(s):
        return Connection(*s.split("-"))


class Path(object):
    """ Object to store current location in a path and small caves that can't be revisited. """

    def __init__(self, loc, path=None):
        """ The path argument, if given, bases this Path on that previous Path. """
        self.loc = loc
        if path is not None:
            # the .copy() is highly necessary, as I discovered only after much pain
            self.small_caves = path.small_caves.copy()
        else:
            self.small_caves = []
        # technically "start" and "end" count as small caves, which should be
        # fine because they are never visited twice anyway
        if loc == loc.lower():
            self.small_caves.append(loc)

    def __str__(self):
        return "path at " + self.loc + " with small cave(s) " + ", ".join(self.small_caves)

    @property
    def double_visit(self):
        """ Return which small cave has been visited twice, or None if none have been visited twice. """
        for c in self.small_caves:
            if self.small_caves.count(c) > 1:
                return c
        return None

    def move(self, newloc):
        """
        Return a new Path equal to the existing one but with a new location.

        Raises a ValueError if newloc is a small cave that has already been visited.
        """
        if (newloc in self.small_caves) and (self.double_visit is not None):
            raise ValueError("Cannot visit " + newloc + ": double visit has already been used on cave " + double_visit)
        return Path(newloc, path=self)


def find_options(cave):
    """
    Given a cave, returns all the caves that could be visited next.

    Even small caves that have already be visited are returned.
    """
    global connections
    return [c[cave] for c in connections if cave in c]

def valid_option(o, path):
    # option not in small caves
    a = o not in path.small_caves
    # option in small caves, but we have room for a double visit
    b = (o != "start") and (o in path.small_caves) and (path.double_visit is None)
    return a or b

def main():
    global connections

    with open("day12_input.txt") as f:
        connections = [Connection.parse(c) for c in f.read().splitlines()]
        f.close()

    # while there are still paths with options remaining
    #   for each path
    #     branch out and make a new path for each valid option
    #       valid options include checking whether the small cave has been visited
    #     delete the path that was branched from
    #     if any path's location is "end"
    #       remove that path from the path list
    #       increment the path counter

    paths = [Path("start")]
    path_count = 0
    while paths:
        # print(f"\n\n\nAt the beginning of iter {iters}:")
        # print("paths =", [str(p) for p in paths])
        # print("path_count =", path_count)

        new_paths = []
        for path in paths:
            # print("\n" + str(path))
            options = find_options(path.loc)
            # print("options", options)

            for o in filter(lambda o: valid_option(o, path), options):
                new_paths.append(path.move(o))
                # print("added", str(new_paths[-1]))

        paths = new_paths.copy()
        prev_len = len(paths)
        # remove paths who have reached the end
        paths = list(filter(lambda p: p.loc != "end", paths))
        # adding the difference adds all the paths that reached the end
        path_count += (prev_len - len(paths))

    print(f"found {path_count} paths")

main()
