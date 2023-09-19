def find_sum(node_index):
    if node_index > len(input_data) - 1:
        return 0

    left_subtree_sum = find_sum(node_index * 2 + 1)
    right_subtree_sum = find_sum(node_index * 2 + 2)

    return left_subtree_sum + right_subtree_sum + input_data[node_index]


def parse_input(input_string):
    data, groups = input_string.split("/")
    input_data = list(map(int, data.split()))
    groups = [list(map(int, group.split())) for group in groups.split(",")]
    return input_data, groups


if __name__ == "__main__":
    input_data, groups = parse_input(input("Enter Input : "))

    sums = []

    total_sum = find_sum(0)

    print(total_sum)

    for group in groups:
        group_sums = []
        for item in group:
            group_sums.append(find_sum(item))
        sums.append(group_sums)

    for i in range(len(groups)):
        if sums[i][0] > sums[i][1]:
            print(f"{groups[i][0]}>{groups[i][1]}")
        elif sums[i][0] < sums[i][1]:
            print(f"{groups[i][0]}<{groups[i][1]}")
        else:
            print(f"{groups[i][0]}={groups[i][1]}")
