def make_album(singer,album):
    album = {'singer':singer.title(),'slbum' : album.upper()}
    return album

album1 = make_album('jay Z','cqgs')
album2 = make_album('TFBOYS','CA')
album3 = make_album('KARRY W','XMA')

print(album1)
print(album2)
print(album3)


