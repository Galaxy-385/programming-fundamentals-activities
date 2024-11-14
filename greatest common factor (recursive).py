#name.py
import functions

print(functions.mcd(135, 40))


#functions.py
def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)
