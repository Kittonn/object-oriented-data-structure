def find_subsets(subset, arr):
    if sum(subset) == target:
        subsets.append(subset)

    for i in range(len(arr)):
        find_subsets(subset + [arr[i]], arr[i + 1 :])

    return subsets


if __name__ == "__main__":
    target, inp = input("Enter Input : ").split("/")
    inp = list(map(int, inp.split()))
    target = int(target)

    subsets = []

    find_subsets([], inp)

    if len(subsets) == 0:
        print("No Subset")
        exit(0)

    for subset in subsets:
        for i in range(len(subset)):
            for j in range(len(subset) - i - 1):
                if subset[j] > subset[j + 1]:
                    subset[j], subset[j + 1] = subset[j + 1], subset[j]

    for i in range(len(subsets)):
        for j in range(len(subsets) - i - 1):
            if len(subsets[j]) > len(subsets[j + 1]):
                subsets[j], subsets[j + 1] = subsets[j + 1], subsets[j]
            elif len(subsets[j]) == len(subsets[j + 1]):
                for k in range(len(subsets[j])):
                    if subsets[j][k] > subsets[j + 1][k]:
                        subsets[j], subsets[j + 1] = subsets[j + 1], subsets[j]
                        break
                    else:
                        break

    for subset in subsets:
        print(subset)
