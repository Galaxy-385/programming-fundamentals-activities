#main.py
import math_utils

l1 = [12, 23, 34, 45, 67, 89]
l2 = [10, 12, 35, 12, 10]
r1 = "IT'S" if math_utils.is_sym(l1) else "IT'S NOT"
print(l1, r1, "SYMMETRIC")
r2 = "IT'S" if math_utils.is_sym(l2) else "IT'S NOT"
print(l2, r2, "SYMMETRIC")

#math_utils.py
def is_sym(l1):
    length = len(l1)
    if l1 == []:
        return True
    elif l1[length - 1] == l1[-length]:
        return is_sym(l1[1:-1])
    elif l1[length - 1] != l1[-length]:
        return False
