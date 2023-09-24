def calculate_min_sum(idx):
    if s[idx] != "*":
        return

    calculate_min_sum(2 * idx + 1)
    calculate_min_sum(2 * idx + 2)

    x = min(s[2 * idx + 1], s[2 * idx + 2])
    s[idx] = x

    s[2 * idx + 1] -= x
    s[2 * idx + 2] -= x


if __name__ == "__main__":
    n, inp = input("Enter Input : ").split("/")
    n = int(n)
    inp = list(map(int, inp.split()))

    if not ((n + 1) // 2 >= len(inp)):
        print("Incorrect Input")
    else:
        s = ["*"] * (n - len(inp))
        s.extend(inp)

        calculate_min_sum(0)

        print(sum(s))
