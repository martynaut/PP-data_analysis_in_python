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
                    #print(dict_entry)
                    #print(result_dataframe.head())
                    df_entry = pd.DataFrame.from_dict(dict_entry, orient='columns')
                    #print(df_entry)
                    result_dataframe = pd.concat([result_dataframe, df_entry], ignore_index=True)
                new_entry = True
                dict_entry = {
                    'Time': np.nan,
                    'Ux': np.nan,
                    'Uy': np.nan,
                    'Uz': np.nan,
                    'p' : np.nan,
                    'nuTilda' : np.nan,
                    'Cd' : np.nan,
                    'Cl' : np.nan
                }
                time_search = re.search(r'Time = ([0-9.e\-]*)', line, re.IGNORECASE)
                if time_search:
                    dict_entry['Time'] = [float(time_search.group(1))]
            else:
                ux_search = re.search(
                r'Solving\sfor\sUx,\sInitial\sresidual\s=\s[0-9.e\-]*,\sFinal\sresidual\s=\s([0-9.e\-]*)',
                    line,
                    re.IGNORECASE)
                if ux_search:
                    dict_entry['Ux'] = [float(ux_search.group(1))]

                uy_search = re.search(
                r'Solving\sfor\sUy,\sInitial\sresidual\s=\s[0-9.e\-]*,\sFinal\sresidual\s=\s([0-9.e\-]*)',
                    line,
                    re.IGNORECASE)
                if uy_search:
                    dict_entry['Uy'] = [float(uy_search.group(1))]

                uz_search = re.search(
                r'Solving\sfor\sUz,\sInitial\sresidual\s=\s[0-9.e\-]*,\sFinal\sresidual\s=\s([0-9.e\-]*)',
                    line,
                    re.IGNORECASE)
                if uz_search:
                    dict_entry['Uz'] = [float(uz_search.group(1))]

                p_search = re.search(
                r'Solving\sfor\sp,\sInitial\sresidual\s=\s[0-9.e\-]*,\sFinal\sresidual\s=\s([0-9.e\-]*)',
                    line,
                    re.IGNORECASE)
                if p_search:
                    dict_entry['p'] = [float(p_search.group(1))]

                nuTilda_search = re.search(
                r'Solving\sfor\snuTilda,\sInitial\sresidual\s=\s[0-9.e\-]*,\sFinal\sresidual\s=\s([0-9.e\-]*)',
                    line,
                    re.IGNORECASE)
                if nuTilda_search:
                    dict_entry['nuTilda'] = [float(nuTilda_search.group(1))]

                Cd_search = re.search(
                r'Cd\s+:\s([0-9.e\-]*)',
                    line,
                    re.IGNORECASE)
                if Cd_search:
                    dict_entry['Cd'] = [float(Cd_search.group(1))]

                Cl_search = re.search(
                r'Cl\s+:\s([0-9.e\-]*)',
                    line,
                    re.IGNORECASE)
                if Cl_search:
                    dict_entry['Cl'] = [float(Cl_search.group(1))]

    #result_dataframe.set_index('Time')[['Cd', 'Cl', 'Ux', 'Uy', 'Uz', 'p', 'nuTilda']]
    print(result_dataframe.tail(5))
    return 0


if __name__ == '__main__':
    read_file('./simple1.log')
