#main
import file_utils
import string_utils

string_utils.save_initials("input.txt", "output.txt")
file_utils.show_file("output.txt")

#string_utils
def save_initials(inp, out):
    with open(inp, 'r') as fi, open(out, 'w') as fo:
        for line in fi:
            lista = []
            for word in line.split():
                lista.append(word[0])
            fo.write(" ".join(lista) + '\n')

#input.txt
'''
this is a
test file 
that stores words
'''
