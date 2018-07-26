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

for item in filelist:
    with open(item, 'r') as f:
        counter = 0
        for line in f:     # line by line
            print (line)
            counter += 1
            #print(counter)

'''nowa_lista = []
for item in filelist:
    if item.endswith('csv.txt'):
        nowa_lista.append(item)
        #print(item)'''
