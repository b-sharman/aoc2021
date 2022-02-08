# what segments each digit uses, in alphabetical order
DIGITS = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

def decode(inp):
    # index this dict by the ideal value to get the real value for a line
    # stands for ideal to real
    idr = {l: list("abcdefg") for l in "abcdefg"}
    # the two unused segments in six-segment digits
    conclusion_069 = []
    # find possibilities based on segments with a unique number of digits
    for segments in inp:
        if len(segments) == spd[1]: # cf
            for char in "cf":
                idr[char] = list(filter(lambda x: x in segments, idr[char]))
            for other_segments in inp:
                # if there's a 7, the segment that the 7 has that the 1 does not have
                # corresponds to the ideal a
                if len(other_segments) == spd[7]:
                    for other_segment in other_segments:
                        if other_segment not in segments: # must be a
                            idr["a"] = [other_segment]
                            break

                # if there's a 4, the two segments that it has and the 1 does not have
                # correspond to either ideal b and d or d and b
                if len(other_segments) == spd[4]: # bcdf
                    b_or_d = []
                    for other_segment in other_segments:
                        if other_segment not in segments: # must be b or d
                            b_or_d.append(other_segment)
                    print("b_or_d", b_or_d)
                    for char in "bd":
                        idr[char] = list(filter(lambda x: x in b_or_d, idr[char]))

                    # also, the three unused segments must be a, e, and g
                    unused = []
                    for segment in "abcdefg":
                        if segment not in other_segments:
                            unused.append(segment)
                    if len(unused) != 3: print("unused", unused)
                    # not going through a; assuming that it is already certain because
                    # of the 1-7 conclusion
                    # for char in "aeg":
                    for char in "eg":
                        idr[char] = list(filter(lambda x: x in unused, idr[char]))

        # For a digit with six segments, which must be a 0, a 6, or a 9, the segment that is not used must be either the ideal c, d, or e.
        if len(segments) == 6:
            for segment in "abcdefg":
                if (segment not in segments) and (segment not in conclusion_069): # it's the unused one
                    conclusion_069.append(segment)

    # For a digit with five segments, which must be a 2, 3, or 5, the ideal a, d, and g must be in those five segments.
    # so we need to find which three segments the digits have in common
    segment_list = list(filter(lambda x: len(x) == 5, inp))
    print("segment_list", segment_list)
    all_the_thingies = []
    for segments in segment_list:
        for segment in segments:
            all_the_thingies += segment
    common_segs = []
    for thingy in all_the_thingies:
        if all_the_thingies.count(thingy) == len(segment_list) and thingy not in common_segs:
            common_segs.append(thingy)
    print("common_segs", common_segs)
    # also, if the 1-7 conclusion has been made, we know which element of segment_list
    # corresponds to ideal a and therefore, the other two elements must correspond to
    # ideal d or g
    if len(idr["a"]) == 1:
        if idr["a"][0] in common_segs:
            common_segs.remove(idr["a"][0])
            print("removed", idr["a"][0])
            print("common_segs is now", common_segs)
        else:
            print("Uh oh")
    for char in "dg":
        idr[char] = list(filter(lambda x: x in common_segs, idr[char]))

    print("conclusion_069", conclusion_069)
    for char in "cde":
        idr[char] = list(filter(lambda x: x in conclusion_069, idr[char]))

    # if we have narrowed down some elements to 1, we know those elements can't
    # be anywhere else
    past_idr = None
    while idr != past_idr:
        for seg_a in idr:
            for seg_b in idr:
                if (seg_a != seg_b) and (len(idr[seg_a]) == 1) and (idr[seg_a][0] in idr[seg_b]):
                    idr[seg_b].remove(idr[seg_a][0])
        past_idr = idr

    if not all([len(x) == 1 for x in idr]):
        raise RuntimeError("didn't narrow down all the possibilities; idr is " + str(idr))

    # instead of the values being one-element lists, make them strings
    # also go the other way
    rdi = {idr[l][0]: l for l in idr}

    # current status: returns possible values for each character, but doesn't
    # do any analysis to further reduce the possibilities
    return rdi

def main():
    global spd

    with open("day8_input.txt") as f:
        inputs = []
        outputs = []
        for line in f.readlines():
            line = line.strip()
            # note to future self: inputs are what you use to form a key
            # outputs are what you use that key to decode
            inputs.append(["".join(sorted(x)) for x in line.split("|")[0].strip().split(" ")])
            outputs.append(["".join(sorted(x)) for x in line.split("|")[1].strip().split(" ")])
        f.close()

    # print(outputs)

    # number of segments that each digit uses
    # 1, 4, 7, and 8 are unique
    spd = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)

    total = 0
    for inp, out in zip(inputs, outputs):
        code = decode(inp)
        print("code", code)
        result = ""
        for o in out:
            decoded = "".join(sorted([code[x] for x in o]))
            result += str(DIGITS.index(decoded))
        print("result", result)
        total += int(result)
        # break # for now, focus on one until I get the algorithm working

    print("\ntotal:", total)

main()
