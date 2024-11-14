#main.py
import math_utils

test_exp = ((56, '+', (5, '*', 2)), '/', (12, '-', 2))
print(math_utils.evaluate(test_exp))


#math_utils.py
def evaluate(datas):
    if isinstance(datas, (int, float)):
        return datas
    if isinstance(datas, tuple) and len(datas) == 3:
        left, operator, right = datas

    left_value = evaluate(left)
    right_value = evaluate(right)

    if operator == "+":
        return left_value + right_value
    elif operator == "-":
        return left_value - right_value
    elif operator == "*":
        return left_value * right_value
    elif operator == "/":
        return left_value / right_value
