#main.py
import string_utils

test_string = "alsikjuyZB8we4 aBBe8XAZ piarBq8 Bq84Z "
test_alphabet = "XYZAB"

print(string_utils.tagger(test_string, test_alphabet))

#string_utils.py
import re


def tagger(text, alphabet):
    return re.sub("([" + alphabet + "]+)", "[target]" + r"\1" + "[endtarget]",
                  text)
