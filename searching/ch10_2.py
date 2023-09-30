def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def searching(target, arr):
    for i in range(len(arr)):
        if arr[i] > target:
            return i
    return None

if __name__ == "__main__":
    inp, targets = input("Enter Input : ").split("/")
    inp = list(map(int, inp.split()))
    targets = list(map(int, targets.split()))

    insertionSort(inp)

    for target in targets:
        idx =  searching(target, inp)
        if idx is not None:
            print(inp[idx])
        else:
            print('No First Greater Value')

        
