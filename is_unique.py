def count_name(name_list, name):
    count = 0
    for value in name_list:
        if value == name:
            count += 1
    return count


def is_unique(name_dct):
    name_values = []

    count = 0
    for key in name_dct:
        name_values.append(name_dct[key])
    for i in range(len(name_values)):
        if count_name(name_values, name_values[i]) > 1:
            count += 1
        else:
            count = 1
    if count > 1:
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

    if is_unique(name_dct2):
        print('The dictionary has unique keys and values.')
    else:
        print('The dictionary is not unique.')


if __name__ == '__main__':
    main()
