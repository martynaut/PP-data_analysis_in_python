import sys
import os, linecache

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

lista_wartosci =[]

'''
for files in nowa_lista:
    with open(files, 'r') as file:
        for line in file:
            if i.isnumeric()==True:
            a = float(i)
            lista_wartosci.append(a)

print(lista_wartosci)
'''
'''
#print(file.readline())
dane = file.readline()
dane = dane.replace(',',' ')
print(dane)
#print(type(file.readline()))
print(type(dane))
'''
'''
for x in range(1,4):
    for file in nowa_lista:
        wiersz = linecache.getline(file, x)
        wiersz = wiersz.replace(',','')
        lista_1  = []
        for i in wiersz:
            lista_1.append(i)

print (lista_1)
'''
lista = []
for files in nowa_lista:
    with open(files, 'r') as file:
        lista_wartosci = file.read().split()
        lista.append(lista_wartosci)

#sumowanie = []
for wiersz in range(3):
    sumowanie = []
    for i in lista:
        c = i[wiersz].replace(',','')
        #print(c)

        for x in c:
            z = float(x)
            sumowanie.append(z)
    suma = sum(sumowanie)
    with open('suma_z_plikow_grzymi.txt','a+') as out_file:
        out_file.write(str(suma)+'\n')
    #print (suma)


#print(sumowanie)



print (nowa_lista)