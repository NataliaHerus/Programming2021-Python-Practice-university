def lucky_numbers(biggest_number, your_condition):
    found_lucky_numbers = []
    for numbers in range(biggest_number):
        string_to_find_figures = str(numbers)
        is_lucky = True
        for position in range(len(string_to_find_figures)):
            is_lucky_digit = False
            for i in range(len(your_condition)):
                if string_to_find_figures[position] == your_condition[i]:
                    is_lucky_digit = True
                    continue
            if not is_lucky_digit:
                is_lucky = False
                break
        if is_lucky:
            found_lucky_numbers.append(string_to_find_figures)
    return len(found_lucky_numbers)


def number():
    while True:
        try:
            the_biggest_number = int(input('Input the biggest natural number: '))
            if the_biggest_number <= 0:
                print('\nLucky numbers are bigger bigger than 0')
                continue
            break
        except ValueError:
            print('\nPlease enter an number')
    return the_biggest_number


def all_for_our_array():
    while True:
        try:
            some_numbers = []
            n = int(input("Input size of array:"))
            if n <= 0:
                print('\nSize should be bigger than 0')
                continue
            for i in range(n):
                array_element = int(input('Input an array element: '))
                some_numbers.append(str(array_element))
                continue
            break
        except ValueError:
            print('\nPlease enter an number')
    return some_numbers


our_number = number()
your_condition = all_for_our_array()
result = lucky_numbers(our_number, your_condition)
print('The amount of lucky numbers less than', our_number, ': ')
if lucky_numbers(our_number, your_condition) == 0:
    print('\nThere are no lucky numbers no larger than the number you entered')
print(result)
