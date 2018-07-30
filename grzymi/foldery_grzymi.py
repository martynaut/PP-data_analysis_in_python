import sys
import os

#print('Number of arguments:', len(sys.argv))
#print('Argument List:', str(sys.argv))

#FOLDER_WITH_DATA = '../data'
FOLDER_WITH_DATA = sys.argv[1]
files = os.walk(FOLDER_WITH_DATA)

#print ([x for x in files])
lista_plikow = []

for krotka in files:
    for file in krotka[2]:
        lista_plikow.append(krotka[0].replace('\\','/')+'/'+file)
        #print (krotka[0].replace('\\','/')+'/'+file)
#print(lista_plikow)


nowa_lista = []
for files in lista_plikow:
    if files.endswith('csv'):
        nowa_lista.append(files)
'''
nowa_lista = []
for files in lista_plikow:
    if files[-3:]=='csv':
        nowa_lista.append(files)
'''

print (nowa_lista)
