import pandas as pd

data = pd.read_excel('https://mdcune.psych.ucla.edu/modules/bioinformatics/extras/QTL_Sample_data.xls')
data_2 = data['sex'].str.replace(' ','').copy()
print(data_2.value_counts())
#print(data, '\n')
#print('Rozmiar tabeli to:', data.shape[0], 'wierszy i', data.shape[1], 'kolumn.', '\n')
#print('Sredni wiek myszy wynosi:', round(data['age'].mean(), 2), 'jednostek.', '\n')
#print('Maksymalna wartość "brainwt" wynosi:', data['brainwt'].max())
#id_myszy = int(input('Podaj ID myszy: '))
#id_sex = data[data['ID']==id_myszy].copy()
#print('Mysz o ID równym', id_myszy, 'jest rodzaju', id_sex.iloc[0]['sex'])
#bodywt_max = data[data['bodywt']==data['bodywt'].max()].copy()
#print('Mysz o najwyzszym "bodywt" ma ID równe:', bodywt_max.iloc[0]['ID'])
#sex_count = data['sex'].value_counts().copy()
#sex_count = data_2['sex'].value_counts().copy()
#print(sex_count)
#print('Jest', sex_count.iloc[0]+sex_count.iloc[2], 'myszy rodzaju zenskiego i', sex_count.iloc[1]+sex_count.iloc[3], 'rodzaju meskiego.')
#print(sex_count.index)
#strain_counts = data['Strain'].unique().copy()
#print('Jest', strain_counts.shape[0], 'rodzajow linii myszy. Rodzaje przedstawione zostaly ponizej:')
#print(data['Strain'].unique())


#https://stackoverflow.com/questions/41476150/removing-space-from-dataframe-columns-in-pandas