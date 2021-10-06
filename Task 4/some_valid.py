def input_element():
    while True:
        try:
            element = int(input('Enter element: '))
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