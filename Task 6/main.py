from Context import Context
from Strategy import *
from Observer import *
import copy


def generate_list(lst, context):
    position = check_pos(lst)
    context = validate_generation(context)
    if isinstance(context.strategy, StrategyIter):
        elements_amount = input_list_size()
    else:
        elements_amount = validate_file()
    cp_ls = copy.deepcopy(lst)
    context.generate_list(lst, position, elements_amount)
    Event("Add", cp_ls, position, lst)


def delete_between(list: LinkedList):
    a, b = segment()
    cp_ls = copy.deepcopy(list)
    list.delete_from_to(a, b)
    Event("Remove", cp_ls, (a, b), list)


def delete_from_pos(list: LinkedList):
    k = input_k()
    cp_ls = copy.deepcopy(list)
    list.delete_element(k)
    Event("Remove", cp_ls, k, list)


def check_pos(lst):
    while True:
        try:
            position = int(input("Enter position: "))
            if lst.is_empty() and position != 0:
                print("The list is empty. Position must be 0")
                continue
            break
        except ValueError:
            print("It must be integer value!")
    return position


def choice():
    list = LinkedList()
    obs = Observer()
    obs.observe('Add')
    obs.observe('Remove')
    context = None
    while True:
        print("Choose what you want:\n"
              "1 - use strategy 1 to insert elements into the list\n"
              "2 - use strategy 2 to insert elements into the list\n"
              "3 - generate list\n"
              "4 - delete element from k-position\n"
              "5 - delete elements between from-to positions\n"
              "6 - find minimum of products multiplications \n"
              "7 - print list\n"
              "8 - exit \n")
        what_chosen = int(input(""))
        if what_chosen == 1:
            context = Context(StrategyIter())
            continue
        elif what_chosen == 2:
            context = Context(StrategyFile())
            continue
        elif what_chosen == 3:
            generate_list(list, context)
            continue
        elif what_chosen == 4:
            delete_from_pos(list)
        elif what_chosen == 5:
            delete_between(list)
        elif what_chosen == 6:
            print(list.minimum(list.__len__()))
        elif what_chosen == 7:
            list.print()
        elif what_chosen == 8:
            break
        else:
            print("Enter right option")
            continue


choice()
