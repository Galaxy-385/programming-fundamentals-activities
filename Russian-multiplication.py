#main.py
import functions

num1 = 5
num2 = 6
prod = functions.product(num1, num2)
print(prod)


#functions.py
def product(num1, num2):
    if num2 == 1:
        return num1
    elif num2 % 2 == 0:
        return product(num1 + num1, num2 // 2)
    else:
        return num1 + product(num1 + num1, num2 // 2)
