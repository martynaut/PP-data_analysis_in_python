
import os.path
import linecache


FOLDER_WITH_DATA = "data/folders_check"
files = os.walk(FOLDER_WITH_DATA)

lista_plikow=[]

for krotka in files:
    for file in krotka[2]:
        lista_plikow.append(krotka[0].replace('\\', '/') + '/' + file)


print(lista_plikow)


nowa = []

for x in lista_plikow:
    if x.endswith("txt"):
        nowa.append(x)

print(nowa)
sumaw=[]
suma=[]

sumaww=0

for k in range(1,4):
        for plik in nowa:

            wiersz = linecache.getline(plik,k)


            for i in wiersz:
                if (i.isnumeric())==True:
                    i=int(i)
                    sumaw.append(i)
                    sumaww=sum(sumaw)

        suma.append(sumaww)

suma[1]=suma[1]-suma[0]
suma[2]=suma[2]-suma[1]-suma[0]
print(suma)

dupa = open('natalia0504/NLEW_wydruk.txt','+w')

for licznik in suma:
    licznik=str(licznik)
    dupa.write(licznik)
    dupa.write("\n")




