from actions_with_linked_list import *


def minimum(lst, size):
    min_multiplication = float('inf')
    for i in range(size - 1):
        if int(lst[i] * lst[i + 1]) < min_multiplication:
            min_multiplication = lst[i] * lst[i + 1]
    return min_multiplication


def input_item():
    item = int(input("Input element you want to insert in list:"))
    return item


def input_k():
    kk = int(input("Input k-position of element:"))
    return kk


def choice():
    while True:
        try:
            print("Choose what you want:\n"
                  "1 - generate list\n"
                  "2 - input list by yourself\n"
                  "3 - insert element at k-position\n"
                  "4 - delete element from k-position\n"
                  "5 - print list\n"
                  "6 - find minimum of products multiplications \n"
                  "7 - exit \n")
            what_chosen = int(input(""))
            if what_chosen == 1:
                list = LinkedList()
                size = list.input_list_size()
                a, b = list.segment()
                list.random_input(size, a, b)
                continue
            elif what_chosen == 2:
                list = LinkedList()
                size = list.input_list_size()
                list.input_list(size)
                continue
            elif what_chosen == 3:
                item = input_item()
                k = input_k()
                list.insert(item, k)
            elif what_chosen == 4:
                k = input_k()
                list.delete_element(k)
            elif what_chosen == 5:
                list.print()
            elif what_chosen == 6:
                size = list.__len__()
                print(minimum(list, size))
            elif what_chosen == 7:
                break
            else:
                print("Enter right option")
                continue

        except ValueError:
            print("Something went wrong, enter an number you want:")


choice()
