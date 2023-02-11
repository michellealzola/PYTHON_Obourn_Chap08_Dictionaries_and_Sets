def max_length(string_set):
    if len(string_set) != 0:
        string_dct = {}
        for word in string_set:
            string_dct[word] = len(word)

        print(string_dct)

        max_word_length = max(string_dct.values())
        max_word = ''
        for k, v in string_dct.items():
            if v == max_word_length:
                max_word = k

        print(f'The word "{max_word}" has the longest string in the set with {max_word_length} characters.')
    else:
        print('The set is empty.')

def main():
    string_set = {'happy', 'gorgeous', 'beautiful', 'lovely', 'kind'}
    max_length(string_set)


if __name__ == '__main__':
    main()
