def make_album(singer,album,number = ''):
    album = {'singer':singer.title(),'slbum' : album.upper()}
    if number:
        album['number'] = number
    return album

album1 = make_album('jay Z','cqgs')
album2 = make_album('TFBOYS','CA',4)
album3 = make_album('KARRY W','XMA',1)

print(album1)
print(album2)
print(album3)


