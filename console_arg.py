import sys


def our_function():

    for arg in sys.argv:
        print(arg)
    print(sys.argv)


if __name__ == '__main__':
    our_function()


# Zadanie: stwórzmy funkcję która liczy długość pliku, którego nazwę podamy jako argument

# Zadanie 2: stwórzmy funkcję która wypisze linię w pliku, którego nazwę podamy jako argument,
# numer linii podany będzie jako drugi argument