#main
import math_utils

my_list = [12, 23, 34, 45, 67, 89]
print(math_utils.list_min(my_list))

#math_utils
def list_min(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        current = numbers[0]
        minor = list_min(numbers[1:])
        return current if current < minor else minor
