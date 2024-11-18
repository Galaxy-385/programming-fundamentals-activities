#main
from functions import caracteres_iguales

# Data to process

string1 = "agua que no has de beber"
string2 = "déjala correr, además es lógico"

# Process and results
resultado = caracteres_iguales(string1, string2)
print(resultado)

#functions
def caracteres_iguales(str1, str2):
    """
    compares two character strings position by position and returns a
    new list where 1 appears in the identical characters in the same
    position on both lists.
    """
    if len(str1) <= len(str2):
        main = str1
        other = str2
    elif len(str1) >= len(str2):
        main = str2
        other = str1
    if len(main) == 0:
        return []
    elif main[0] == other[0]:
        return [1] + caracteres_iguales(str1[1:], str2[1:])
    elif main[0] != other[0]:
        return [0] + caracteres_iguales(str1[1:], str2[1:])
