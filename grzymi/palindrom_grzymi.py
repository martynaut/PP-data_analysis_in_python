'''
a = [1, 2, 3, 4]
b = []
for i in reversed(a):
    b.append(i)

print(b)
'''

def palindrom(fraza='kajak'):
    fraza = fraza.lower().replace(' ', '')
    nowa_fraza = []
    for i in fraza:
        nowa_fraza.append(i)
    #print(nowa_fraza)
    fraza_odwrocona = []
    for i in reversed(nowa_fraza):
        fraza_odwrocona.append(i)
    #print(fraza_odwrocona)
    if nowa_fraza == fraza_odwrocona:
        return print('Podana przez Ciebie fraza jest palindromem.')
    else:
        return print('Podana przez Ciebie fraza jest nie palindromem.')
        
print ('Witaj w programie, ktory sprawdza, czy fraza/slowo jest palindromem.')
fraza = input('Podaj fraze/slowo, ktore chcesz sprawdzic: ')
palindrom (fraza=fraza)