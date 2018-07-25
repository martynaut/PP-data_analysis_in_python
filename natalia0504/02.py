
"""
Zadanie 1.1.
Otwórz projekt w PyCharm i stwórz plik seriale.py

W skrypcie stwórz zmienną o nazwie seriale.

Przypisz do niej listę zawierającą tytuły seriali (min. 8)
Wypisz pierwszy serial na liście
Wypisz 7 serial na liście
Wypisz ostatni serial na liście
Wypisz pierwsze cztery seriale na liście
Wypisz cztery ostatnie seriale na liście
Wypisz seriale na pozycjach od 4 do 7
"""

seriale=["breaking bad","star trek","battlestar","doctor who","expanse","narcos","broadchurch","family guy"]

print(seriale[0])
print(seriale[6])
print(seriale[-1])
print(seriale[:4])
print(seriale[-4:])
print(seriale[3:7:1])
print("\n")

"""
Zadanie 1.2.
Stwórz plik klienci.py

Stwórz zmienną liczba_klientow
Przypisz jej listę z pięcioma przykładowymi liczbami (liczba klientów danego dnia)
Stwórz zmienną wczoraj i przypisz jej ostatnią liczbę z listy liczba_klientow
Wykorzystując funkcję input() stwórz zmienna dzis i zapytaj użytkownika ile klientów było dzisiaj (zmienna dzis)
Wykorzystując funkcję append() dodaj liczbę ze zmiennej dzis do listy liczba_klientow
"""

liczba_klientow=[34,56,65,32,56]
print(liczba_klientow)
wczoraj=liczba_klientow[-1]
dzis=input('Podaj, ilu klientow bylo dzisiaj:')
liczba_klientow.append(dzis)
dzis=int(dzis)
print(liczba_klientow)



Zadanie 4.1. - update zadania 1.2
Otwórz plik klienci.py
Wykorzystując instrukcje warunkowe (if..else...) sprawdź czy liczba klientów jest 
większa czy mniejsza niż wczoraj i wyświetl tę informację użytkownikowi


if(wczoraj>dzis):
    print("wczoraj bylo wiecej klientow")
elif(wczoraj==dzis):
    print("dzis jest tyle samo klientow co wczoraj")
else: print("dzisiaj jest wiecej klientow niz wczoraj")
print("\n")


Zadanie 4.2.
Napisz program, który zapyta użytkownika o jego rok urodzenia, a następnie wypisze je na ekranie.
Jeżeli rok urodzenia > 2000 niech wypisze rok urodzenia
W przeciwnym przypadku niech wypisze “Dobrze, ze jestes pelnoletni”


wiek=input("Podaj rok urodzenia:")
wiek=int(wiek)
if(wiek>2000):
    print(wiek)
else:
    print("Dobrz, ze jestes pelnoletni")

"""
"""
Zadanie 4.3.
Pani Wiesia ma mnóstwo kwiatów do przygotowania z okazji zakończenia szkoły. W celu usprawnienia 
tego procesu pani Wiesia postanowiła pogrupować bukiety w zależności od koloru i liczby kwiatów w bukiecie.
Zaimplementuj program który:
Wczyta od użytkownika liczbę kwiatów
Wczyta od użytkownika kolor kwatów
Sprawdzi czy liczba kwiatów jest nieparzysta i poinformuje o tym użytkownika
Wypisze liczbę kwiatów i kolor
Wypisze komunikat, jeżeli kwiatów >50 i <= 100, że bukiet będzie drogi
Wypisze komunikat, jeżeli kwiatów >100, że bukiet będzie za ciężki


liczba=input("Podaj liczbe kwiatow:")
liczba=int(liczba)
kolor=input("Podaj kolor kwiatow:")
if(liczba%2!=0):
    print("Liczba kwiatow jest nieparzysta")
print("Zamowiles kwiaty w ilosci:",liczba,"\nZamowiony kolor kwiatow:",kolor)
if(liczba>50 and liczba<=100):
    print("bukiet bedzie drogi")
elif(liczba>100):
    print("bukiet bedzie za ciezki")


"""

"""
Zadanie 5.1¶
Wyświetl wszystkie liczby parzyste z przedziału 0-26
"""

"""
for i in range(1,27):
    print(i)
"""

"""
Zadanie 5.2
Wypisz powitanie dla każdej osoby z listy ("Cześć <
osoby = ["Monika", "Wojciech", "Jan", "Piotr", "Agata"]
"""

"""
osoby = ["Monika", "Wojciech", "Jan", "Piotr", "Agata"]
for i in osoby:
    print("Witaj",i,"!")
"""

"""
Zadanie 5.3
Sprawdź, który znak w ciągu "Ala ma 4 koty" jest liczbą.
"""

for i in "ala ma 4 koty":
    if(i<"a"):
        print(i)


print("kupa")

#kupa

