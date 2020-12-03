import re
# def convert(new_words):
#     vowels = r'[AEIOUaeiou]'
#     consonants = r'[BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz]'
#     new_words = new_words.split(' ')
#     vow = new_words[0::3]
#     new_str = " ".join(vow)
#     replacement = '%'
#     output = re.sub(vowels, replacement, new_str)
#     output = list(output.split(" "))
#     new_conso = new_words[1::3]
#     new_conso = ' '.join(new_conso)
#     rep = '#'
#     ou = re.sub(consonants, rep, new_conso)
#     ou = list(ou.split(" "))
#     third_word = new_words[2::3]
#     third_word = ' '.join(third_word).upper()
#     third_word = list(third_word.split(" "))
#     final_list = output + ou + third_word
#     # print(final_list)
#     print(' '.join(final_list))
#
# convert('Where are you? Meet me near the clock tower')

def funct1(new_words):
    vowels = r'[aeiouAEIOU]'
    consonants = r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]'
    new_words = new_words.split(" ")
    vow = new_words[0::3]
    new_line = " ".join(vow)
    replacement = "*"
    output = re.sub(vowels, replacement, new_line)
    output = list(output.split(" "))
    cons = new_words[1::3]
    cons = " ".join(cons)
    replace = "#"
    out1 = re.sub(consonants, replace, cons)
    out1 = list(out1.split(" "))
    third_word = new_words[2::3]
    third_word = " ".join(third_word).upper()
    third_word = list(third_word.split(" "))
    final_list = output + out1 + third_word
    print(" ".join(final_list))

funct1('Where are you? meet me near the clock tower!')


