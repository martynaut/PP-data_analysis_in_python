import os
import sys

FOLDER_WITH_DATA = sys.argv[1]
files = os.walk(FOLDER_WITH_DATA)

lista_plikow = []

for krotka in files:
    for file in krotka[2]:
        lista_plikow.append(krotka[0].replace('\\', '/')+'/'+file)
print(lista_plikow)

new_lista = []
for x in lista_plikow:
    if x[-3:] == 'csv':
        new_lista.append(x)

# new_lista = [x for x in lista_plikow if 'dataset_1' in x]


print(new_lista)

# - po kolei lista krotek: nazwa lokalizacji, foldery w lokalizacji, pliki w lokalizacji
