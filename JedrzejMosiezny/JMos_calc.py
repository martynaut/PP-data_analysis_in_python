import calc_func as cf

def calc(*args, funkcja='suma'):
    if funkcja=='srednia':
        return cf.srednia(*args)
    elif funkcja=='minimum':
        return cf.minimum(*args)
    else:
        return cf.suma(*args)

print("To jest absolutnie niepraktyczny kalkulator")
funkcja = str(input("Podaj operację (suma*, srednia, minimum): "))

f_lista = ('', 'suma', 'srednia', 'minimum')
if funkcja not in f_lista:
    funkcja = str(input("Podaj właściwą operację (suma*, srednia, minimum): "))
elif funkcja == '':
    funkcja = 'suma'

print("Podaj argumenty funkcji, zakoncz argumentem end")
argumenty = []
argument = 0

while argument != 'end':
    argument = input()
    if argument == 'end':
        break
    else:
        try:
            argument = float(argument)
        except:
            print("tylko liczby lub 'end'")
            argument = input()
    argumenty.append(argument)

argumenty = tuple(map(float, (argumenty[:-1])))
print("Wynik operacji " + str(funkcja) + " na liczbach: " + str(argumenty) + " to:")
print(calc(argumenty, funkcja=funkcja))