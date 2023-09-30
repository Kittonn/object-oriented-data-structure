def find_alphabet_chars(word):
    return [char for char in word if char.islower()]

if __name__ == '__main__':
    word_list = input("Enter Input : ").split()

    for i in range(len(word_list)):
        for j in range(len(word_list) - i - 1):
            alpha1 = find_alphabet_chars(word_list[j])
            alpha2 = find_alphabet_chars(word_list[j + 1])

            if alpha1 > alpha2:
                word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]

    print(*word_list)
