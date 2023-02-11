def reverse(data_dct):
    name_set = set()
    for v in data_dct.values():
        name_set.add(v)

    name_arrange = {}
    for name in name_set:
        num_data = []
        for k, v in data_dct.items():
            if name == v:
                num_data.append(k)
            name_arrange[name] = num_data

    print(name_arrange)


def main():
    data_dct = {42: "Marty",
                81: "Sue",
                17: "Ed",
                31: "Dave",
                56: "Ed",
                3: "Marty",
                29: "Ed"}

    reverse(data_dct)


if __name__ == '__main__':
    main()
