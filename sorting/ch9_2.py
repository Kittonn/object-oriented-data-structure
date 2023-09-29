def insertMinHeap(h, i):
    pass

def delMin(h, last):
    pass

h = []
a = input("Enter list of number: ").split(",")
for i in range(len(a)):
    h.append(int(a[i]))
    insertMinHeap(h, i)

print("Heap: ", end="")
print(*h)
print("==== heap sort ====")
for last in range(len(h)-1, 0, -1):
    delMin(h, last)
print("==== Sorting a ====")
h.reverse()
print(*h)