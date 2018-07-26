import funkcje_kalkulatora as fk

def calc(*args, funkcja='suma'):
    if funkcja=='srednia':
        return fk.srednia(*args)
    elif funkcja=='minimum':
        return fk.minimum(*args)
    else:
        return fk.suma(*args)

print ('Wybierz funkcje. Do wyboru masz: suma, srednia, minimum:')
funkcja = str(input())
f_lista = ('', 'suma', 'srednia', 'minimum')
while funkcja not in f_lista:
    funkcja = str(input('Podaj prawidlowa nazwe funkcji: suma, srednia, minimum:'))
if funkcja == '':
    funkcja = 'suma'


argumenty = []
argument = 0
while argument!='end':
    print('Podaj liczby, na ktorych chcesz wykonac operacje:')
    argument = input()
    if argument == 'end':
        break
    else:
        try:
            argument = float(argument)
            argumenty.append(argument)
        except ValueError:
            print ('Podales zmienna innego typu niz oczekiwana.')

argumenty = tuple(argumenty)
print(argumenty)

print (calc(argumenty,funkcja=funkcja))