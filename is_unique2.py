def is_unique(name_dct):
    name_values = {}
    count_duplicate = 0
    for k, v in name_dct.items():
        if v in name_values:
            name_values[v] += 1
            count_duplicate += 1
        else:
            name_values[v] = 1
            count_duplicate = 1

    print('The name count:')
    for name in name_values:
        print(f'{name}: {name_values[name]}')

    if count_duplicate > 1:
        return False
    else:
        return True


def main():
    name_dct = {"Kendrick": "Perkins",
                "Stuart": "Reges",
                "Jessica": "Wolk",
                "Bruce": "Reges",
                "Hal": "Perkins"}

    name_dct2 = {"Kendrick": "Smith",
                 "Stuart": "Reges",
                 "Jessica": "Wolk",
                 "Bruce": "Charles",
                 "Hal": "Perkins"}

    if is_unique(name_dct):
        print('The dictionary has unique keys and values.')
    else:
        print('The dictionary is not unique.')

    print()
    if is_unique(name_dct2):
        print('The dictionary has unique keys and values.')
    else:
        print('The dictionary is not unique.')


if __name__ == '__main__':
    main()
