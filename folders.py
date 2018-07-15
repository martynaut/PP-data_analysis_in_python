import os

FOLDER_WITH_DATA = '.'
files = os.walk(FOLDER_WITH_DATA)
print(files)

# print([x for x in files]) # - po kolei lista krotek: nazwa lokalizacji, foldery w lokalizacji, pliki w lokalizacji
