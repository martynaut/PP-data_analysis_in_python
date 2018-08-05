import pandas as pd
import os

FOLDER_WITH_DATA = './data'
files = os.walk(FOLDER_WITH_DATA)

lista_plikow = []
for krotka in files:
    for file in krotka[2]:
        if file.endswith('.txt'):
            lista_plikow.append(krotka[0].replace('\\','/')+'/'+file)

# non-pandas
with open('sumowanie_non_pandas', 'w+') as output_file:
    results = []
    for file in lista_plikow:
        counter = 1
        with open(file) as input_file:
            for line in input_file:
                if counter > len(results):
                    results.append(sum(list(map(int, line.strip().split(',')))))
                else:
                    results[counter-1] += sum(list(map(int, line.strip().split(','))))
                counter += 1
    for line in results:
        output_file.write(str(line)+'\n')



# pandas
results = pd.DataFrame()
for files in lista_plikow:
    if results.shape[0] == 0:
        results = pd.read_csv(files, header=None).sum(axis=1)
    else:
        results = results+pd.read_csv(files, header=None).sum(axis=1)
results.to_csv('sumowanie_pandas', index=False)
