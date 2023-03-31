#!/usr/bin/python

import string
from itertools import product
import os
import math
from tqdm import tqdm

caracteres = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

def gerar_wordlist(caracteres, min_len, max_len):
    counter = 0
    file_size = 0
    for i in range(min_len, max_len+1):
        file_size += len(caracteres) ** i
    file_size *= (1 - (len(caracteres) - 1) / len(caracteres))  # remove passwords with three consecutive characters
    file_size /= 1024**2  # convert to megabytes
    print("Estimated file size: {:.2f} MB".format(file_size))

    with open("wordlist.txt", "w") as file:
        for i in range(min_len, max_len+1):
            for j in tqdm(product(caracteres, repeat=i), desc="Generating passwords", unit=" passwords"):
                word = "".join(j)
                if not tem_tres_consecutivos_iguais(word):
                    file.write(word + '\n')
                    counter += 1

    print("Wordlist of {} passwords created".format(counter))

def tem_tres_consecutivos_iguais(word):
    consecutivos = 1
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            consecutivos += 1
            if consecutivos == 3:
                return True
        else:
            consecutivos = 1
    return False

min_len = int(input("Digite o mínimo de caracteres: "))
max_len = int(input("Digite o máximo de caracteres: "))
gerar_wordlist(caracteres, min_len, max_len)
