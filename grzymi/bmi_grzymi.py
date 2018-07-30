waga = input('Podaj swoja wage w kg: ')

try:
    waga = float(waga)
except ValueError:
    print ('Zly typ danych')

wzrost = input('Podaj swoj wzrost w metrach: ')

try:
    wzrost = float(wzrost)
except ValueError:
    print ('Zly typ danych')

try:
    bmi = waga/(wzrost**2)
    print(bmi)
except ZeroDivisionError:
    print('Przez 0. Serio?')

#print(bmi)#Komentarz do pliku