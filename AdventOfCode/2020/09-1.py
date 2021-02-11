from pprint import pprint

def to_list(fh):
    nums = []
    for line in fh:
        line = line.split('\n')[0]
        nums.append(int(line))
    return nums

def find_sums(splice):
    sums = []
    for i, num in enumerate(splice):
        for j, num2 in enumerate(splice):
            if i != j:
                sums.append(num + num2)
    return sums

def find_invalid(nums, limit, i):
    if nums[i] not in find_sums(nums[i - limit : i]):
        return nums[i]
    return find_invalid(nums, limit, i + 1)

def main():
    with open('data.txt', 'r') as fh:
        nums = to_list(fh)
        invalid = find_invalid(nums, 25, 25)
        print(invalid)


if __name__ == "__main__":
    main()