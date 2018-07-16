no_flowers = int(input('Z ilu kwiatow chcesz bukiet? '))
color_flowers = input('Jakiego kolory maja byc kwiaty? ')

if no_flowers%2==1:
    print ('Twoj bukiet bedzie sie skladal z nieparzystej liczby kwiatow.')
else:
    print('Twoj bukiet bedzie sie skladal z parzystej liczby kwiatow.')

if no_flowers<=50:
    print ('Twoj bukiet bedzie sie skladal z ' + str(no_flowers) + ' ' + color_flowers + ' kwiatow.')
elif no_flowers>50 and no_flowers<=100:
    print('Twoj bukiet bedzie sie skladal z ' + str(no_flowers) + ' ' + color_flowers + ' kwiatow i bedzie drogi.')
elif no_flowers>100:
    print('Twoj bukiet bedzie sie skladal z ' + str(no_flowers) + ' ' + color_flowers + ' kwiatow, bedzie drogi i bardzo ciezki.')