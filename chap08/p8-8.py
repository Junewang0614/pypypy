def make_album(singer,album):
    album = {'singer':singer.title(),'album' : album.upper()}
    return album
while True:
    singer = input()
    if singer == 'q':
        break
    album = input()
    if album == 'q':
        break

    make_album = make_album(singer,album)
    print(make_album)


