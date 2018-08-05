'''
otworzyć po kolei każdy z tych plików
stworzyć nowy plik file_sum.csv zawierający sumę z każdej linijki z każdego pliku
'''

import os.path
import os
import sys

FOLDER_WITH_DATA = 'data/folders_check'
files = os.walk(FOLDER_WITH_DATA)
#print(list(files))

filelist = []
for krotka in files:
    for file in krotka[2]:
        filelist.append(krotka[0].replace('\\', '/') + '/' + file)
        #print(krotka[0].replace('\\', '/')  + '/' + file)

if os.path.isfile('data/sum.csv'):
    file = open('data/sum.csv', 'a')

else:
    file = open('data/sum.csv', "w+")
suma0 = [0, 0, 0]
suma1 = [0, 0, 0]
suma2 = [0, 0, 0]
for item in filelist:
    with open(item, 'r') as f:
        for idx, line in enumerate(f):     # line by line
            globals()['line%s' % idx] = [float(x) for x in line.strip().split(",")]
            #print(line%s % idx)
        suma0 = [x + y for x, y in zip(suma0, line0)]
        suma1 = [x + y for x, y in zip(suma1, line1)]
        suma2 = [x + y for x, y in zip(suma2, line2)]

print(suma0)
print(suma1)
print(suma2)

'''nowa_lista = []
for item in filelist:
    if item.endswith('csv.txt'):
        nowa_lista.append(item)
        #print(item)'''
