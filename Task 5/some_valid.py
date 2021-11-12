import os


def validate_file(end=".txt"):
    while True:
        try:
            filename = input("Enter file name: ")
            if not os.path.isfile(filename) and not filename.endswith(end):
                print("There's no such" + filename + " file")
                continue
            break
        except ValueError:
            print("Incorrect symbols")
    return filename


def validate_generation(context):
    if context == None:
        raise UnboundLocalError("You need to choose type of generation and after do another options.")
    return context


def input_list_size():
    while True:
        try:
            list_size = int(input('Input an amount of elements: '))
            if list_size <= 2:
                print('\nAmount should be bigger than 2')
                continue
            break
        except ValueError:
            print("Please enter an integer number")
    return list_size


def segment():
    a = int(input('Enter the first space item: '))
    b = int(input('Enter the second space item: '))
    check_from_to(a, b)
    return a, b


def check_from_to(a, b):
    while True:
        if a > b:
            a, b = b, a
            print('\nThe first number should not be  bigger than the second, so we swapped them')
        break


def input_integer():
    while True:
        try:
            element = int(input('Enter integer number: '))
            return element
            break
        except ValueError:
            print("Please enter an integer number")


def input_item():
    item = int(input("Input element you want to insert in list:"))
    return item


def input_k():
    k = int(input("Input k-position of element:"))
    return k
