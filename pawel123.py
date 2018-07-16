import os.path


with open('data/retail-food-stores.csv', 'r') as f:
    counter = 0
    for line in f:     # line by line
        counter += 1
print(counter)

if os.path.isfile('data/newfile.txt'):
    file = open('data/newfile.txt', 'a')

else:
    file = open('data/newfile.txt', "w+")
file.write('something\n')
