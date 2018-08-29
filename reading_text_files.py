import pandas as pd
import numpy as np
import re

def read_file(file_name):
    result_dataframe = pd.DataFrame(columns=[
        'Time',
        'Ux',
        'Uy'
    ])
    new_entry = False
    with open(file_name) as f:
        for line in f:
            if line.startswith('Time ='):
                if new_entry:
                    print(dict_entry)
                    print(result_dataframe.head())
                    df_entry = pd.DataFrame.from_dict(dict_entry, orient='columns')
                    print(df_entry)
                    result_dataframe = pd.concat([result_dataframe, df_entry], ignore_index=True)
                new_entry = True
                dict_entry = {
                    'Time': np.nan,
                    'Ux': np.nan,
                    'Uy': np.nan
                }
                time_search = re.search(r'Time = ([0-9]*)', line, re.IGNORECASE)
                if time_search:
                    dict_entry['Time'] = [int(time_search.group(1))]
            else:
                ux_search = re.search(
                r'GAMG:\s\sSolving\sfor\sUx,\sInitial\sresidual\s=\s[0-9.e\-]*,\sFinal\sresidual\s=\s([0-9.e\-]*)',
                    line,
                    re.IGNORECASE)
                if ux_search:
                    dict_entry['Ux'] = [float(ux_search.group(1))]

    return 0


if __name__ == '__main__':
    read_file('./simple1.log')
