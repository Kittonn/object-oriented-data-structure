def search_row_min(inp):
    min = inp[0]
    for i in range(1, len(inp)):
        if inp[i] < min:
            min = inp[i]
    return inp.index(min) // table[0]


if __name__ == "__main__":
    table, inp = input("input : ").split(",")
    table = list(map(int, table.split()))
    inp = list(map(int, inp.split()))

    search = search_row_min(inp)

    find_col = search % table[0]

    print(search)
