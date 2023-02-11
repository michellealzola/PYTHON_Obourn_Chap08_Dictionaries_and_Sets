def max_occurrence(number_list):
    number_dct = {}
    for num in number_list:
        if num in number_dct:
            number_dct[num] += 1
        else:
            number_dct[num] = 1

    max_value = max(number_dct.values())
    max_key = ''
    for k, v in number_dct.items():
        if v == max_value:
            max_key = k

    print(f'The key:value with maximum occurrence is {max_key}:{max_value}')


def main():
    number_list = [10, 1, 6, 4, 8, 7, 8, 5, 10, 6, 10, 9, 7, 8, 1, 5, 6, 4, 7, 10]
    max_occurrence(number_list)


if __name__ == '__main__':
    main()
