from random import randint


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


def input_number(matrix_size):
    while True:
        try:
            matrix = []
            for i in range(matrix_size):
                elements = []
                for j in range(matrix_size):
                    elements.append(int(input("Input a matrix element: ")))
                matrix.append(elements)
            break
        except ValueError:
            print("Please enter an integer number")
    return matrix


def create_matrix():
    print("Your matrix is: ")
    matrix_size = check_size()
    matrix = input_number(matrix_size)
    return matrix_size, matrix


def segment():
    a = int(input('Enter the first space item: '))
    b = int(input('Enter the second space item: '))
    check_from_to(a, b)
    return a, b


def check_from_to(a, b):
    while True:
        if b < a:
            print('\nThe first number should not be  bigger than the second')
        break


def random_input(matrix, matrix_size, a, b):
    for i in range(matrix_size):
        arr = []
        for j in range(matrix_size):
            arr.append(randint(a, b))
        matrix.append(arr)
    return arr


def print_matrix(matrix, matrix_size):
    for i in range(matrix_size):
        for j in range(matrix_size):
            print(matrix[i][j], end=" ")
        print()


def sort_bubble(array, size):
    quantity = 0
    for i in range(size):
        for j in range(size):
            m, n = i, j + 1
            while True:
                if n == size:
                    n = 0
                    m += 1
                    if m == size:
                        break
                if array[i][j] > array[m][n]:
                    swap_value = array[i][j]
                    array[i][j] = array[m][n]
                    array[m][n] = swap_value
                    quantity += 1
                n += 1
    print("Amount of operations to sort matrix: ", quantity)


def find_index(matrix, item):
    lowest_to_find = 0
    highest_to_find = len(matrix)
    while lowest_to_find < highest_to_find:
        middle = (lowest_to_find + highest_to_find) // 2
        mid_val = matrix[middle]
        if item > mid_val:
            lowest_to_find = middle + 1
        else:
            highest_to_find = middle
    return lowest_to_find


def binary_search(matrix, element):
    goal = [row[-1] for row in matrix]
    index1 = find_index(goal, element)
    search = False
    if index1 != len(goal):
        row = matrix[index1]
        index2 = find_index(row, element)
        if index2 != len(row) and row[index2] == element:
            search = True
    if search:
        print("Firstly we found ", element, 'in', " ( ", index1, index2, " )")
    if not search:
        print("There are no such element in matrix")


def choice():
    while True:
        try:
            matrix = []
            print("Choose what you want:\n"
                  "1 - input matrix by yourself, see it and do binary search\n"
                  "2 - generate matrix, see it and do binary search\n"
                  "3 - exit \n")
            what_chosen = int(input(""))
            if what_chosen == 1:
                matrix_size, matrix = create_matrix()
            elif what_chosen == 2:
                matrix_size = check_size()
                a, b = segment()
                random_input(matrix, matrix_size, a, b)
            elif what_chosen == 3:
                break
            else:
                print("Enter right option")
                continue
            do(matrix, matrix_size)
        except ValueError:
            print("Something went wrong, enter an number you want:")


def do(matrix, matrix_size):
    print_matrix(matrix, matrix_size)
    sort_bubble(matrix, matrix_size)
    print_matrix(matrix, matrix_size)
    element = int(input('Input an element you want to find:'))
    binary_search(matrix, element)


choice()
