#main
import number_functions

numbers1 = [3, 5, 4, 3, 6]
numbers2 = [2, 3, 5, 6, 2]
sun_numbers = number_functions.sum_lists(numbers1, numbers2)
print(sun_numbers)

#number_functions
def sum_lists(num1, num2):
    if not num1 and not num2:
        return []
    else:
        return [num1[0] + num2[0]] + sum_lists(num1[1:], num2[1:])
