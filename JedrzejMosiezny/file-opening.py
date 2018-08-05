import os.path
import os
import sys

#print('Number of arguments:', len(sys.argv))
#print('Argument List:', str(sys.argv))
'''
#Zad 1
with open('JMos_new.py', 'a') as f:
f.write('\n#something\n')

#Zad 2
#FOLDER_WITH_DATA = '../data/folders_check'
FOLDER_WITH_DATA = 'data/folders_check'
files = os.walk(FOLDER_WITH_DATA)

#print(list(files))

filelist = []
for krotka in files:
    for file in krotka[2]:
        filelist.append(krotka[0].replace('\\', '/') + '/' + file)
        #print(krotka[0].replace('\\', '/')  + '/' + file)

#print(filelist)    

nowa_lista = []
for item in filelist:
    if 'dataset_1' in item:
        nowa_lista.append(item)
        #print(item)

print(nowa_lista)

#Zad 3
FOLDER_WITH_DATA = 'data'
files2 = os.walk(FOLDER_WITH_DATA)
#print(list(files))

filelist2 = []
for krotka2 in files2:
    for file in krotka2[2]:
        filelist2.append(krotka2[0].replace('\\', '/') + '/' + file)
        #print(krotka[0].replace('\\', '/')  + '/' + file)

nowa_lista2 = []
for item in filelist2:
    if item.endswith('csv'):
        nowa_lista2.append(item2)
        #print(item)
'''
#FOLDER_WITH_DATA = '../data/folders_check'
FOLDER_WITH_DATA = str(sys.argv[1])
files = os.walk(FOLDER_WITH_DATA)

#print(list(files))

filelist = []
for krotka in files:
    for file in krotka[2]:
        filelist.append(krotka[0].replace('\\', '/') + '/' + file)
        print(krotka[0].replace('\\', '/')  + '/' + file)

#print(filelist)    

'''nowa_lista = []
for item in filelist:
    if 'dataset_1' in item:
        nowa_lista.append(item)
        #print(item)

print(nowa_lista)'''