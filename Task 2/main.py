import random


def check_size():
    while True:
        try:
            matrix_size = int(input('Input matrix size: '))
            if matrix_size < 2:
                print('\nSize should be bigger than 2')
                continue
            break
        except ValueError:
            print("Please enter an integer positive number")

    return matrix_size


def input_data(matrix):
    while True:
        try:
            matrix_size = check_size()
            print("Your matrix is: ")
            for i in range(matrix_size):
                elements = []
                for j in range(matrix_size):
                    elements.append(int(input("Input a matrix element: ")))
                matrix.append(elements)
            break
        except ValueError:
            print("Please enter an integer number")
    return matrix_size


def random_input(matrix, matrix_size):
    while True:
        try:
            a = int(input('Enter the first space item: '))
            b = int(input('Enter the second space item: '))
            if b < a:
                print('\nThe first number should not be  bigger than the second')
                continue
            break
        except ValueError:
            print("Please enter an integer number")
    for i in range(matrix_size):
        arr = []
        for j in range(matrix_size):
            arr.append(random.randint(a, b))
        matrix.append(arr)


def print_matrix(matrix, matrix_size):
    for i in range(matrix_size):
        for j in range(matrix_size):
            print(matrix[i][j], end=" ")
        print()


def sort_bubble(array, size):
    swap_value = 0
    quantity = 0
    exit = False
    while not exit:
        exit = True
        for i in range(size):
            for j in range(size - 1):
                if array[i][j] > array[i][j + 1]:
                    swap_value = array[i][j]
                    array[i][j] = array[i][j + 1]
                    array[i][j + 1] = swap_value
                    quantity += 1
                    exit = False
                if i != size - 1 and j == size - 2:
                    if array[i][j + 1] > array[i + 1][0]:
                        swap_value = array[i][j + 1]
                        array[i][j + 1] = array[i + 1][0]
                        array[i + 1][0] = swap_value
                        quantity += 1
    print("Amount of operations to sort matrix: ", quantity)


def find_index(matrix, item):
    lowest_to_find = 0
    highest_to_find = len(matrix)
    while lowest_to_find < highest_to_find:
        middle = (lowest_to_find + highest_to_find) // 2
        mid_val = matrix[middle]
        if item > mid_val:
            lowest_to_find = + 1
        else:
            highest_to_find = middle
    return lowest_to_find


def binary_search(matrix, element):
    goal = [row[-1] for row in matrix]
    index1 = find_index(goal, element)
    if index1 != len(goal):
        row = matrix[index1]
        index2 = find_index(row, element)
        if index2 != len(row) and row[index2] == element:
            search = True
        else:
            search = False
    if search:
        print("Firstly we found ", element, 'in', " ( ", index1, index2, " )")
    if not search:
        print("There are no such element in matrix")


def choice():
    while True:
            try:
                print("Choose what you want:\n"
                      "1 - input matrix by yourself, see it and do binary search\n"
                      "2 - generate matrix, see it and do binary search\n"
                      "3 - exit \n")
                what_chosed = int(input(""))
                if what_chosed == 1:
                    matrix = []
                    matrix_size = input_data(matrix)
                    print_matrix(matrix, matrix_size)
                    sort_bubble(matrix, matrix_size)
                    print_matrix(matrix, matrix_size)
                    element = int(input('Input an element you want to find:'))
                    binary_search(matrix, element)
                    continue
                elif what_chosed == 2:
                    matrix = []
                    matrix_size = check_size()
                    random_input(matrix, matrix_size)
                    print_matrix(matrix, matrix_size)
                    sort_bubble(matrix, matrix_size)
                    print_matrix(matrix, matrix_size)
                    element = int(input('Input an element you want to find:'))
                    binary_search(matrix, element)
                    continue
                elif what_chosed == 3:
                    break
            except ValueError:
                print("Something went wrong, enter an number you want:")
                continue
            except KeyboardInterrupt:
                print("Something went wrong, enter an number you want:")
                continue
            break


choice()
