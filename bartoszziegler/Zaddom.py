from Funkcja import *

def calc(Y, funkcja='suma'):
    if funkcja=='srednia':
        return srednia(Y)
    elif funkcja=='minimum':
        return minimum(Y)
    else:
        return suma(Y)
print ('Wybierz funkcje. Do wyboru masz: suma, srednia, minimum:')
funkcja = str(input())
f_lista = ('', 'suma', 'srednia', 'minimum')
while funkcja not in f_lista:
    funkcja = str(input('Podaj prawidlowa nazwe funkcji: suma, srednia, minimum:'))
if funkcja == '':
    funkcja = 'suma'
print('Podaj liczby, na ktorych chcesz wykonac operacje, rozdziel je spacjami!:')
argumenty = list(float(x) for x in input().split(' '))
print("twoje argumenty to" +str(argumenty))
print ("wynik wybranej operacji to "+str(calc(argumenty,funkcja=funkcja)))