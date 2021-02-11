from collections import Counter

def calc_jolt_differences(jolts):
    diffs = []
    for j1, j2 in zip( jolts[1:] + [max(jolts) + 3], jolts ):
        diffs.append(j1 - j2)
    return diffs

def main():
    to_list = lambda fh : [ int(line[ : len(line) - 1 ]) for line in fh if line[ : len( line ) - 1].isnumeric()] 
    with open('data.txt', 'r') as fh:
        jolts = to_list(fh)
        jolts.append(0)
        jolts.sort()
        diffs = calc_jolt_differences(jolts)
        diffs = Counter(diffs)
        print(diffs)
        print(diffs[1] * diffs[3])


if __name__ == "__main__":
    main()