def rarest(number_dct):
    number_list = []
    for value in number_dct.values():
        number_list.append(value)

    number_only_dct = {}
    for num in number_list:
        if num in number_only_dct:
            number_only_dct[num] += 1
        else:
            number_only_dct[num] = 1

    print(number_only_dct)

    min_value = min(number_only_dct.values())
    min_key = ''
    for k, v in number_only_dct.items():
        if v == min_value:
            min_key = k

    print(f'The key:value with minimum occurrence is {min_key}:{min_value}')


def main():
    number_dct = {'a': 10, 'b': 1, 'c': 6,
                  'd': 4, 'e': 8, 'f': 7,
                  'g': 8, 'h': 5, 'i': 10,
                  'j': 6, 'k': 10, 'l': 9,
                  'm': 7, 'n': 8, 'o': 1,
                  'p': 5, 'q': 6, 'r': 4,
                  's': 7, 't': 10}

    rarest(number_dct)


if __name__ == '__main__':
    main()
