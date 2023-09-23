def partition(arr, low, high, ascending=True):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if (arr[j] <= pivot) if ascending else (arr[j] >= pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high, ascending=True):
    if low < high:
        pi = partition(arr, low, high, ascending)
        quick_sort(arr, low, pi - 1, ascending)
        quick_sort(arr, pi + 1, high, ascending)

if __name__ == "__main__":
    inp = input("Enter Input : ").split()
    split_str = [ord(j) for i in inp for j in i if j.islower()]
    
    quick_sort(split_str, 0, len(split_str) - 1, ascending=True)

    result = ' '.join([j for i in split_str for j in inp if chr(i) in j])
    print(result)