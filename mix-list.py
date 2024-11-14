#main.py
import math_utils

l1 = [12, 23, 34, 45, 67, 89]
l2 = [10, 12, 35, 43, 65]
print(math_utils.merge(l1, l2))


#math_utils
def merge(l1, l2):
    if not l1 and not l2:
        return []
    if not l1:
        return l2[:]
    if not l2:
        return l1[:]
    if l1[0] > l2[0]:
        return [l2[0]] + merge(l1, l2[1:])
    elif l1[0] < l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l1[0], l2[0]] + merge(l1[1:], l2[1:])
