def is_unique(name_dct):
    name_values = []
    for k, v in name_dct.items():
        name_values.append(v)
    name_set = set(name_values)
    if len(name_values) > len(name_set):
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
