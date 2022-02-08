"""
Psuedocode

parse the input into line objects
find the most extreme values
make a grid big enough to hold all the lines
for each line,
    increment each spot on the grid that holds that line
count the number of locations on the grid holding 2 or greater
"""

class Lanternfish(object):
    """ A fish that reproduces every n days. """

    def __init__(self, days_left:int):
        # days left to reproduce
        self.days_left = days_left

    def __repr__(self):
        return str(self.days_left)

    def update(self):
        """
        Call every day.

        Returns a new Lanternfish if a new Lanternfish has spawned,
        otherwise None.
        """
        self.days_left -= 1
        if self.days_left < 0:
            # start the cycle again after 7 days
            self.days_left = 6
            # new Lanternfish have 2 extra days to reach sexual maturity
            return Lanternfish(8)
        return None

def main():
    with open("day6_input.txt") as f:
        fishes = [Lanternfish(int(n)) for n in f.read().strip().split(",")]
        f.close()

    print(fishes)
    num_days = 80
    for day in range(num_days, 0, -1):
        new_fishes = []
        for fish in fishes:
            new_fish = fish.update()
            if new_fish is not None:
                new_fishes.append(new_fish)
        fishes += new_fishes
        # print(fishes)

    print(len(fishes), "fish exist")
        
main()
