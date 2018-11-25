def make_shirt(size,word = 'I love python.'):
    print('THE SHIRT IS ' + size.upper() + '.')
    print('"' + word.upper() + '"' + ' IS ON THE SHIRT.')
#大号默认
make_shirt('l')
#中号默认
make_shirt(size = 'm')
#其它字样
make_shirt(size = 'xxl',word = 'whatever')

