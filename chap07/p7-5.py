message = ''

while message != 'quit':
    age = input('HOW OLD ARE YOU ? ')
    print('THE PRICE IS :')
    if int(age) < 3:
        print('$0')
    elif (int(age) >=3) and (int(age) <= 12):
        print('$10')
    elif(int(age) >= 12):
        print('$15')

    message = input('quit or not? ')

