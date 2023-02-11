def symmetric_set_difference(set1, set2):
    num_list = []
    for num in set1:
        num_list.append(num)
    for num2 in set2:
        num_list.append(num2)

    num_dct = {}
    for number in num_list:
        if number in num_dct:
            num_dct[number] += 1
        else:
            num_dct[number] = 1

    set3 = set()
    for k, v in num_dct.items():
        if v == 1:
            set3.add(k)

    print(set3)


def main():
    set1 = {1, 4, 7, 9}
    set2 = {2, 4, 5, 6, 7}

    symmetric_set_difference(set1, set2)


if __name__ == '__main__':
    main()
