def odd_list(al):
    return [i for i in al if i % 2 != 0]


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]

opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)