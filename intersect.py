def intersect(name_dct1, name_dct2):
    name_intersect = {}
    for name in name_dct1:
        for name2 in name_dct2:
            if name == name2 and name_dct1[name] == name_dct2[name2]:
                name_intersect[name] = name_dct1[name]
    print(name_intersect)


def main():
    name_dct1 = {"Janet": 87, "Logan": 62, "Whitaker": 46, "Alyssa": 100,
                 "Stef": 80, "Jeff": 88, "Kim": 52, "Sylvia": 95}
    name_dct2 = {"Logan": 62, "Kim": 52, "Whitaker": 52, "Jeff": 88,
                 "Stef": 80, "Brian": 60, "Lisa": 83, "Sylvia": 87}

    intersect(name_dct1, name_dct2)


if __name__ == '__main__':
    main()
