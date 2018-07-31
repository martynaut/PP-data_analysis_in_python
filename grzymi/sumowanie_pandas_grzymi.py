import pandas as pd
import numpy as np
import os

FOLDER_WITH_DATA = '../data'
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
    if files.endswith('.txt'):
        nowa_lista.append(files)
#print(nowa_lista)

#lista_wartosci =[]
size_check = pd.read_csv(nowa_lista[0], names=['A', 'B', 'C'])
print(size_check.shape)

suma = np.zeros(size_check.shape, np.int32)
print(suma, '\n')

for files in nowa_lista:
    data = pd.read_csv(files, names=['A', 'B', 'C'])
    suma = suma+data
    #print (data, '\n')

suma = suma.sum(axis=1)
print (suma)
suma.to_csv('sumowanie_pandas', index=False)