
import pandas as pd
from pprint import pprint

lista_1 = [1,2,3]
pd.Series(data=lista_1)

lista_2 = ['a', 'b', 'c']
pd.Series(data=lista_2)

lista_3 = [1, 2, 'c', 4]
pd.Series(data=lista_3)

pd.Series(data=lista_3, index=lista_2)

pprint(lista_1)
pprint(lista_2)
pprint(lista_3)


