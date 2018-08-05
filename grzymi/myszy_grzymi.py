import pandas as pd

data = pd.read_excel('https://mdcune.psych.ucla.edu/modules/bioinformatics/extras/QTL_Sample_data.xls')
data['sex'] = data['sex'].str.replace(' ','').copy() #zamienia spacje na puste znaki w kolumnie 'SEX'
print(data, '\n') #wyswietla tabele
print('Rozmiar tabeli to:', data.shape[0], 'wierszy i', data.shape[1], 'kolumn.', '\n') #Wyswietla rozmiar tabeli
print('Sredni wiek myszy wynosi:', round(data['age'].mean(), 2), 'jednostek.', '\n') #oblicza i wyswietla sredni wiek myszy
print('Maksymalna wartość "brainwt" wynosi:', data['brainwt'].max()) #znajduje i wyswietla najwyzsza wartosc 'BRAINWT'

id_sex = data[data['ID']==1709].copy()
print('Mysz o ID 1709 jest rodzaju', id_sex.iloc[0]['sex'])

bodywt_max = data[data['bodywt']==data['bodywt'].max()].copy() #znalezienie myszy o najwyzszym 'BODYWT' i wyswietlenie jej ID
print('Mysz o najwyzszym "bodywt" ma ID równe:', bodywt_max.iloc[0]['ID'])

#Okreslenie, ile jest myszy, a ile myszow
sex_count = data['sex'].value_counts().copy()
print(sex_count)
print('Jest', sex_count.iloc[0], 'myszy rodzaju zenskiego i', sex_count.iloc[1], 'rodzaju meskiego.')
#print(sex_count.index)

#okreslenie ilosci rodzajow myszy
strain_counts = data['Strain'].unique().copy()
print('Jest', strain_counts.shape[0], 'rodzajow linii myszy. Rodzaje przedstawione zostaly ponizej:')
print(data['Strain'].unique())

male_mouse = data[data['sex']=='M']
female_mouse = data[data['sex']=='F']
print('Srednie wartosci "bodywt" i "brainwt" dla myszy rodzaju meskiego to odpowiednio:', round(male_mouse['bodywt'].mean(),2), 'i', round(male_mouse['brainwt'].mean(),2))
print('Srednie wartosci "bodywt" i "brainwt" dla myszy rodzaju zenskiego to odpowiednio:', round(female_mouse['bodywt'].mean(),2), 'i', round(female_mouse['brainwt'].mean(),2))

#https://stackoverflow.com/questions/41476150/removing-space-from-dataframe-columns-in-pandas