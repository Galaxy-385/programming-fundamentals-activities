#main.py
import string_utils

names = ['John', 'Paul', 'Martin', 'Peter', 'Max', 'Mia']
initial = 'M'
filtered_names = string_utils.filter_names(names, initial)
print(filtered_names)


#string_utils.py
def filter_names(names, initial):
    if len(names) == 0:
        return []
    elif names[0][0] != initial:
        return filter_names(names[1:], initial)
    elif names[0][0] == initial:
        return [names[0]] + filter_names(names[1:], initial)
