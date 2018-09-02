# Kurs Pythona -  Politechnika Poznańska 07-09 2018
### Podsumowanie
##### Prowadzący: Martyna Urbanek-Trzeciak


## 1. Basic Python commands
#### 1.1. Definiowanie zmiennych

`zmienna = 1`

`zmienna_tekstowa = 'text'`

#### 1.2. Sprawdzenie typu

`type(zmienna)`

#### 1.3. Listy, słowniki

`lista = [1, 2, 3, 'tekst']`

`słownik = {
    1: 'jeden',
    2: 'dwa'
}`

##### 1.3.1. Slice listy
[odkąd(włącznie):dokąd(wyłącznie):co_ile]

`lista[0:5:2]`

##### 1.3.2. Lista od tyłu

`lista[::-1]`

##### 1.3.3. Listy i słowniki można zagnieżdżać

`lista = [1, [4, 5, [7]]]`

##### 1.3.4. Dodawanie do listy
`lista.append('element')`

`lista.expand(['element1', 'element2'])`

##### 1.3.4. Iterowanie po elementach słownika

```
for key, value in słownik.items():
    print(key, value)
```

##### 1.3.5. Dodawanie do słownika

`słownik['nowy_klucz'] = 'nowa wartość'`

#### 1.4. Warunek if/else

```
if a == True:
    do_something()
elif b == True:
    do_something_else()
else:
    do_nothing()
```

#### 1.5. Funkcje matematyczne
```
1+1
2-5
2/4
2*4
2**7
2%2
```
#### 1.6. Zmiana typu
```
int(7.0)
bool(1)
float(5)
```

#### 1.7. Inne funkcje wbudowane

```
max([1,2,3])
min([4,5,6])
sum([6,7,8])
```

#### 1.8.  Pobieranie treści od użytkownika

`imie_uzytkownika = input("Jak masz na imię?")`

#### 1.9.  Porównywanie

```
a == b
a <= g
a > g
a != v
```

`a is b` (wskazują ten sam element w pamięci)

#### 1.10.  Pętla for

```
for i in [1,2,3]:
    print(i)
```

#### 1.11. Pętla while

```
while a < 5:
    print(a)
    a =+ 1
```

#### 1.12.  Definiowanie funkcji

```
def function_name(argument1, argument2=2, *args, **kwargs):
    print(argument1, argument2, args, kwargs)
```

### 2. Skrypty złożone
#### 2.1. Importowanie paczek i modułów

```
import numpy
import numpy as np
from matplotlib import pyplot
```

#### 2.2. Korzystanie ze skryptów konsolowych

```
#!/usr/bin/env python
import sys


def our_function():

    for arg in sys.argv: # pozwala na dostanie się do elementów podanych w konsoli
        print(arg)
    print(sys.argv)


if __name__ == '__main__': # zapobiega odpalaniu funcjonalności w momencie improtu
    our_function()
```

#### 2.3. Praca z plikami

```
import os.path

with open('data/retail-food-stores.csv', 'r') as f: # odczyt
    counter = 0
    for line in f:     # line by line - nie wczytujemy całości
        counter += 1
print(counter)

if os.path.isfile('data/newfile.txt'):
    file = open('data/newfile.txt', 'a') # dopisywanie do pliku

else:
    file = open('data/newfile.txt', "w+") # zapis do pliku
file.write('something\n')
```


#### 2.4. Wędrówka po folderach

`files = os.walk(FOLDER_WITH_DATA)`

#### 2.5. Wyjątki

```
def add(x, y):
    try:
        int(x + y)
    except TypeError:
        print('wrong types added')
    except ValueError:
        print('cannot change to int type')


add('a', 'b')
```

#### 2.5. Pamięciożerność i czasożerność

dwie przydatne biblioteki:
* tracemalloc
* time

```
def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))

tracemalloc.start()
start = time.clock()

nasza_funkcjonalność()

snapshot = tracemalloc.take_snapshot()
display_top(snapshot)
stop = time.clock()

print('finished in', stop-start, 'seconds')
```

### 3. Numpy, Pandas i Matplotlib

#### 3.1. Wstęp do Numpy

##### 3.1.1. Array

```
lista = [1,2,3]
lista_list = [[1,2,3],[4,5,6],[7,8,9]]

array_1d = np.array(lista)
array_2d = np.array(lista_list)

np.arange(0,10)
np.zeros(4)
np.linspace(0,1,10)
np.random.rand(3,3)

# zmiana wymiarów
array_1d.reshape(3,1)
print(array_1d.shape)


# slice'y
array_2d[:2, 1:]
```

##### 3.1.2. Macierz

`matrix_2d = np.matrix(lista_list)`

#### 3.2. Wstęp do Pandas

##### 3.2.1. Wczytanie
`df = pd.read_csv('file.csv')`

##### 3.2.2. Podgląd
`df.head()`
`df.tail()`

##### 3.2.3. Nowa kolumna
`df['name'] = 1`

##### 3.2.4. Usunięcie kolumny
`df.drop('columns_name', axis=1, inplace=True)`

##### 3.2.5. Wybranie wierszy spełniających warunek

`df[df['columns_name']<2]`

##### 3.2.6. Wyciągnięcie fragmentu kolumny typu object (str)
`df['columns_name'].str.extract('([0-9]*)', expand=False')`

##### 3.2.7. Zamiana typu

`df['column_name'].astype(int)`

##### 3.2.8. Grupowanie

```
df2 = df.groupby('column').sum()
df2 = df.groupby('columns').agg(lambda x: x.sum())
df2.reset_index(inplace=True)
```

##### 3.2.9. Nieznane wartości

```
df.fillna(0)
df.dropna(inplace=true)
```

##### 3.2.10. Łączenie Data Frames

```
df.join(df2, on='column_name') # jak join w SQLu
pd.concat([df,df2]) # dwie DataFrame z takimi samymi kolumnami pod sobą
```

##### 3.2.11. Zapis
`df.to_csv('file_name.csv')`

##### 3.2.12. Apply i lambda
```df['column_new'] = df['base_column'].apply(lambda x: x**2)```

#### 3.3. Wstęp do Matplotlib


##### 3.3.1 Plot bezpośrednio z DataFrame'u
``` 
df['column'].plot()
plt.xlim(0,1)
plt.ylim(0,1)
plt.title('title')
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.show()
```


##### 3.3.2 Przykład subplots

```
fig, axes = plt.subplots(2,1, sharex=True, figsize = (6,4))

# przerwy między subplotami
plt.subplots_adjust(wspace=0, hspace=0)

axes[0].plot(a, color='r')
axes[1].plot(b, color='g')

# ticksy
axes[1].set_xlim(0,100)
start, end = axes[1].get_xlim()
axes[1].xaxis.set_ticks(np.arange(start, end+1, 10))

axes[0].set_ylim(0,1000)
start, end = axes[0].get_ylim()
axes[0].yaxis.set_ticks(np.arange(start, end+1, 500))

axes[1].set_ylim(0,5000)
start, end = axes[1].get_ylim()
axes[1].yaxis.set_ticks(np.arange(start, 4001, 1000))

# usuwanie linii
axes[1].spines['top'].set_visible(False)

axes[0].set_title('two sublots with single x axis')

plt.show()
```
##### 3.3.2 Obrazek w obrębie wykresu

```
imgplot = plt.imshow(img)
plt.show()
```

### 4. Wielowątkowość i wieloprocesowość

#### 4.1. Wielowątkowość - przykład

Wykorzystanie biblioteki threading

```
import threading
from queue import Queue
import requests
import bs4
import time

print_lock = threading.Lock()

def get_url(current_url):

    with print_lock:
        print("\nStarting thread {}".format(threading.current_thread().name))
    res = requests.get(current_url)
    res.raise_for_status()

    current_page = bs4.BeautifulSoup(res.text,"html.parser")
    current_title = current_page.select('title')[0].getText()

    with print_lock:
        print("{}\n".format(threading.current_thread().name))
        print("{}\n".format(current_url))
        print("{}\n".format(current_title))
        print("\nFinished fetching : {}".format(current_url))

def process_queue():
    while True:
        current_url = url_queue.get()
        get_url(current_url)
        url_queue.task_done()

url_queue = Queue()

url_list = ["https://www.github.com"]*5

for i in range(5):
    t = threading.Thread(target=process_queue)
    t.daemon = True
    t.start()

for current_url in url_list:
    url_queue.put(current_url)

url_queue.join()

``` 
#### 4.2. Wieloprocesowość - przykład

Wykorzystanie biblioteki multiprocessing

```
from multiprocessing import Pool, freeze_support
import time

def sum_num(num1, num2):

    return num1 + num2


start = time.time()
freeze_support() # Potrzebne na Windowsie
if __name__ == '__main__':
    with Pool(2) as p:
        print(p.starmap(sum_num, zip([1,3,5], [2,4,6])))
print("Time taken = {0:.5f}".format(time.time() - start))
```

### 5. Dask

Dask pozwala na wstępną definicję skryptu i dopiero wykonanie, 
dzięki czemu lepiej zarządza zasobami

```
from dask import delayed
x = delayed(fun1)(1,2)
y = delayed(fun2)(1,2)
z = delayed(fun1)(x,y)
z.compute() # dopiero tutaj komendy są wykonywane
```

#### 5.1. Praca z Dask DataFrame

```
import dask.dataframe as dd
df = dd.read_csv('file_*.csv')
final_max = df['2'].max().compute()
```

zamiast

```
filenames = ['file_1.csv', 'file_2.csv', 'file_3.csv', 'file_4.csv']

maxes = []
for fn in filenames:
    p_df = pd.read_csv(fn)
    maxes.append(p_df['2'].max())

final_max = max(maxes)
final_max
```

