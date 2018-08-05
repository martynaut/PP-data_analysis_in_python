import os.path
import os
import sys
from pprint import pprint
import pandas as pd
import dask.dataframe as dd
import numpy as np

FOLDER_WITH_DATA = 'data/folders_check'
files = os.walk(FOLDER_WITH_DATA)
#print(list(files))

filelist = []
for krotka in files:
    for file in krotka[2]:
        filelist.append(krotka[0].replace('\\', '/') + '/' + file)
        #print(krotka[0].replace('\\', '/')  + '/' + file)

batch_data = dd.read_csv(filelist)
pprint(batch_data)
sum1 = batch_data.sum(axis=0).compute()
pprint(sum1)