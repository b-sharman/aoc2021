import time
import numpy as np

NUM_DAYS = 256

def main():
    time0 = time.time()
    nums = np.loadtxt("day6_input.txt", dtype=np.int64, delimiter=",")
    time1 = time.time()
    print("read and parsed data in", round(time1-time0, 4), "s")

    # index this by i to find out how many fish are at i
    # for example, num_of_each[8] returns the number of fish at 8
    #
    # this value of num_of_each discovers how many fish a single fish makes
    # after NUM_DAYS days
    num_of_each = np.array((0, 1, 0, 0, 0, 0, 0, 0, 0))
    # number of fish that the single fish made during the last five days
    last_five = np.zeros(5, dtype=np.int64)
    for i in range(NUM_DAYS):
        num_of_each = np.roll(num_of_each, -1)
        # The number of 6s currently only counts the fish that were 7s
        # last time. This adds the zeros that turned into 6s.
        num_of_each[6] += num_of_each[-1]
        # populate last_five if we are in the last five days
        if i >= NUM_DAYS - 5:
            last_five[i-NUM_DAYS+5] = num_of_each.sum()

    # for each fish, find out how many fish it results in after NUM_DAYS
    # days and then add those results together
    #
    # https://numpy.org/doc/stable/user/basics.indexing.html#index-arrays
    print("end with", last_five[-nums].sum(), "fish in", round(time.time()-time1, 4), "s")

main()
