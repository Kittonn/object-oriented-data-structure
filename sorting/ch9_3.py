def check_asc(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

def check_desc(lst):
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            return False
    return True

def check_unique(lst):
    return len(set(lst)) == len(lst)

def check_drome(is_asc, is_desc, is_unique):
    if is_asc and is_desc and not is_unique:
        return "Repdrome"
    elif is_asc and is_unique:
        return "Metadrome"
    elif is_desc and is_unique:
        return "Katadrome"
    elif is_desc and not is_unique:
        return "Nialpdrome"
    elif is_asc and not is_unique:
        return "Plaindrome"
    else:
        return "Nondrome"

if __name__ == "__main__":
    inp = input("Enter Input : ")
    inps = [int(i) for i in inp]
    
    is_asc = check_asc(inps)
    is_desc = check_desc(inps)
    is_unique = check_unique(inps)

    print(check_drome(is_asc, is_desc, is_unique))
    
