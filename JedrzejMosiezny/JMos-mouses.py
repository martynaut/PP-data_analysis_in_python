import pandas as pd
import numpy as np
from pprint import pprint

#wczytanie dataframe, wysortowanie po ID, zmiana indeksu na ID
mouse = pd.read_excel('https://mdcune.psych.ucla.edu/modules/bioinformatics/extras/QTL_Sample_data.xls',shee_tname='Sheet1').sort_values(by='ID').set_index('ID')
pprint(mouse) #sprawdzenie struktury tabeli

#czyszczenie stringów
mouse_obj = mouse.select_dtypes(['object'])
mouse[mouse_obj.columns] = mouse_obj.apply(lambda x: x.str.strip())
pprint(mouse) #sprawdzenie nowej struktury tabeli

mouse_age_mean = mouse['age'].mean()
pprint("Sredni wiek myszy: " + str(mouse_age_mean)) #średni wiek

mouse_brainwt_max = mouse['brainwt'].max()
pprint("Maksymalna waga mozgu myszy: " + str(mouse_brainwt_max)) #maksymalny brainwt

mouse_1709_sex = mouse.loc[1709,'sex']
pprint("Plec myszy 1709: " + str(mouse_1709_sex)) #płeć myszy 1709

mouse_max_bodywt = mouse['bodywt'][mouse['bodywt'] == mouse['bodywt'].max()] 
pprint("Indeks najcięższej myszy: " + str(mouse_max_bodywt.index.values[0])) #maksymalna waga myszy

mouse_sex_count = mouse['sex'].value_counts()
pprint("Jest " + str(mouse_sex_count[0]) + " samcow") #rozkład płci
pprint("Jest " + str(mouse_sex_count[1]) + " samic") #rozkład płci

strain_mouse = np.array(mouse['Strain'].unique())
print("Jest: " + str(strain_mouse.size) + " typow myszy")

mouse_f_bodywt_mean = mouse['bodywt'][mouse['sex'] == 'F'].mean()
mouse_f_brainwt_mean = mouse['brainwt'][mouse['sex'] == 'F'].mean()
print("Sredni bodywt samic: " + str(mouse_f_bodywt_mean))
print("Sredni brainwt samic: " + str(mouse_f_brainwt_mean))

mouse_m_bodywt_mean = mouse['bodywt'][mouse['sex'] == 'M'].mean()
mouse_m_brainwt_mean = mouse['brainwt'][mouse['sex'] == 'M'].mean()
print("Sredni bodywt samcow: " + str(mouse_m_bodywt_mean))
print("Sredni brainwt samcow: " + str(mouse_m_brainwt_mean))