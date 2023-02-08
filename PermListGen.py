#!/usr/bin/python
from itertools import permutations
from itertools import product
import string 

min_len = int(input("Digite o mínimo de caracteres: "))
max_len = int(input("Digite o máximo de caracteres: "))
counter = 0
caracter = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

file_open = open("Wordlist.txt", "w")

for i in range (min_len,max_len+1):
    for j in product(caracter,repeat=i):
        word = "".join(j)
        file_open.write(word)
        file_open.write('\n')
        counter+=1
print("Wordlist of {} password created".format(counter))
