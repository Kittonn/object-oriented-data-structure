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

def find_subsets(temp_arr, data):
    if sum(temp_arr) == s:
        ans_arr.append(temp_arr)
        
    
    for i in range(len(data)):
        find_subsets(temp_arr + [data[i]], data[i+1:])

    return ans_arr
    

if __name__ == '__main__':
    s, inp = input('Enter Input : ').split('/')

    s = int(s)
    inp = [int(i) for i in inp.split()]

    ans_arr = []
    find_subsets([], inp)

    if len(ans_arr) == 0:
        print('No Subset')
    else:
        for i in ans_arr:
            quick_sort(i, 0, len(i) - 1, ascending=True)

        for l in range(len(ans_arr) - 1, 0, -1):
            for i in range(l):
                if len(ans_arr[i]) > len(ans_arr[i + 1]):
                    ans_arr[i], ans_arr[i + 1] = ans_arr[i + 1], ans_arr[i]
                elif len(ans_arr[i]) == len(ans_arr[i + 1]):
                    for j in range(len(ans_arr[i])):
                        if ans_arr[i][j] > ans_arr[i + 1][j]:
                            ans_arr[i], ans_arr[i + 1] = ans_arr[i + 1], ans_arr[i]
                            break
                        elif ans_arr[i][j] < ans_arr[i + 1][j]:
                            break
                        
        for i in ans_arr:
            print(i)


