import pandas as pd
import os
import time
import zipfile

start = time.time()

with zipfile.ZipFile("data.zip","r") as zip_ref:
    zip_ref.extractall(".")

FOLDER_WITH_DATA = '.'
files = os.walk(FOLDER_WITH_DATA)
#print ([x for x in files])

#print('pliki', files)

lista_plikow = []

for krotka in files:
    for file in krotka[2]:
        lista_plikow.append(krotka[0].replace('\\','/')+'/'+file)

#print('lista plikow = ', lista_plikow)

def poziom(level):
    poziom = []
    for files in lista_plikow:
        if files.startswith('./p'+str(level)+'/p'):
            poziom.append(files)
    return poziom

print(poziom(1))

total = pd.DataFrame()

for x in poziom(1):
    df = pd.read_csv(x, sep='\t', skiprows=23, usecols=[1,2,3,4,5,6,7,8,9,16,17], names=['T1','T2','T3','T4','T5','T6','T7','T8','Tsuction','CO2','O2'], decimal=',')
    #ave = df.tail(10)
    file_name = x[5:]
    #print (file_name, '\n', df.tail(10).mean(axis=0).transpose())
    ave = df.tail(10).mean(axis=0)
    total = total.append(ave, ignore_index=True)


print(total.set_index(poziom(1)))

end = time.time()
print('Czas działania programu = ', round((end-start)*1000,4), 'ms')

#https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.append.html