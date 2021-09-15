def lucky_numbers(biggest_number):
    lucky_numbers = []
    array_to_help_find = []
    for numbers in range(biggest_number):
        string_to_find_figures = str(numbers)
        for position in range(len(string_to_find_figures)):
            if '4' in string_to_find_figures[position] or '7' in string_to_find_figures[position]:
                array_to_help_find.append(string_to_find_figures[position])
            else:
                array_to_help_find.clear()
                break

        if len(array_to_help_find) != 0:
            result = [int(item) for item in array_to_help_find]
            lucky_numbers.append(result)
    return len(lucky_numbers)


def input_data():
    while True:
        try:
            the_biggest_number = int(input('Input the biggest natural number: '))
            if the_biggest_number <= 0:
                print('\nLucky numbers are bigger than 0')
                continue
            break
        except ValueError:
            print('\nPlease enter an number')
    return the_biggest_number


our_number = input_data()
found_lucky_numbers = lucky_numbers(our_number)
print('The amount of lucky numbers less than', our_number, ': ')
if lucky_numbers(our_number) == 0:
    print('\nThere are no lucky numbers no larger than the number you entered')
print(found_lucky_numbers)
