active = True
message = ''

while active:
    age = input('HOW OLD ARE YOU ? ')
    if age == 'quit':
        break
    print('THE PRICE IS :')
    if int(age) < 3:
        print('$0')
    elif (int(age) >=3) and (int(age) <= 12):
        print('$10')
    elif(int(age) >= 12):
        print('$15')

    message = input('quit or not? ')
    if message == 'quit':
        active = False


