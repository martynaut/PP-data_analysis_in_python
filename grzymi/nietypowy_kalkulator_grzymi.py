def suma(*args):
    s = sum(args)
    return s

def srednia(*args):
    av = sum(args)/len(args)
    return av

def minimum(*args):
    mini = min(args)
    return mini

def calc(*args, funkcja='suma'):
    if funkcja=='srednia':
        return srednia(*args)
    elif funkcja=='minimum':
        return minimum(*args)
    else:
        return suma(*args)

#argumetny = ()
#while argumenty!='end':
print ('Wybierz funkcje. Do wyboru masz: suma, srednia, minimum:')
funkcja = str(input())
f_lista = ('', 'suma', 'srednia', 'minimum')
while funkcja not in f_lista:
    funkcja = str(input('Podaj prawidlowa nazwe funkcji: suma, srednia, minimum:'))
if funkcja == '':
    funkcja = 'suma'
print('Podaj liczby, na ktorych chcesz wykonac operacje:')
argumenty = input()



print (calc(argumenty,funkcja=funkcja))