#main.py
import file_utils
import string_utils

string_utils.no_empty_lines("input.txt", "output.txt")
file_utils.show_file("output.txt")

#string_utils.py
def no_empty_lines(inp, out):
    with open(inp, "r") as fi:
        lines = fi.readlines()
        nop_empty_l = [line for line in lines if line.strip()]
    with open(out, "w") as fo:
        fo.writelines(nop_empty_l)

#input.txt
'''
water is important for life


my friend

aurora lives in europe

also mike
'''
