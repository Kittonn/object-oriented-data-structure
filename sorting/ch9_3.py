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

def is_palindrome_type(arr):
    sorted_arr_asc = arr.copy()
    sorted_arr_desc = arr.copy()
    
    quick_sort(sorted_arr_asc, 0, len(sorted_arr_asc) - 1, ascending=True)
    quick_sort(sorted_arr_desc, 0, len(sorted_arr_desc) - 1, ascending=False)
    
    if arr == sorted_arr_asc and arr == sorted_arr_desc:
        return "Repdrome"
    elif arr == sorted_arr_asc:
        return "Plaindrome" if len(set(arr)) != len(arr) else "Metadrome"
    elif arr == sorted_arr_desc:
        return "Nialpdrome" if len(set(arr)) != len(arr) else "Katadrome"
    else:
        return "Nondrome"

if __name__ == "__main__":
    inp = input("Enter Input : ")
    inps = [int(i) for i in inp]
    
    result = is_palindrome_type(inps)
    print(result)
