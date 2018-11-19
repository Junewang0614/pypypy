places = {}

polling_active = True

while polling_active:
    name = input('\nwhat is your name? ')
    place = input('what is your dreaming place for vacation? ')

    places[name] = place

    repeat = input('would you like to ler another person respond? (yes/no) ')
    if (repeat == 'no'):
        polling_active = False

print('\n--- poll results ---')

for name,place in places.items():
    print(name + ' would like to go to ' + place + '.')
