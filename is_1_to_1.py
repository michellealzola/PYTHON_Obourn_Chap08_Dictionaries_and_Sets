def is_1_to_1(phonebook):
    phone_numbers = set()
    for v in phonebook.values():
        phone_numbers.add(v)
    if len(phonebook) > len(phone_numbers):
        return False
    else:
        return True


def main():
    phonebook = {"Marty": "206-9024", "Hawking": "555-1234",
                 "Smith": "949-0504", "Newton": "123-4567"}

    if is_1_to_1(phonebook):
        print("The dictionary's keys map to unique values")
    else:
        print("Some of the dictionary's keys map to the same values")


if __name__ == '__main__':
    main()
