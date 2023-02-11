def has_odd(number_set):
    if len(number_set) != 0:
        odd_number_list = []
        for num in number_set:
            if num % 2 != 0:
                odd_number_list.append(num)

        if len(odd_number_list) > 0:
            return True
        else:
            return False

    else:
        print('The set is empty')


def main():
    number_list = [10, 1, 6, 4, 8, 7, 8, 5, 10, 6, 10, 9, 7, 8, 1, 5, 6, 4, 7, 10]
    number_set = set(number_list)
    if has_odd(number_set):
        print(f'(True) The set {number_set} has at least one odd number')
    else:
        print('(False) The set does not have any odd number.')






if __name__ == '__main__':
    main()
