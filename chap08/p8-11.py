def show_magician(magician_names):
    for magician in magician_names:
        print(magician)

def make_great(magicians_old,magicians_new):
    while magicians_old:
        magician = ('the Great ' + magicians_old.pop())
        magicians_new.append(magician)

magicians_old = ['lh','lq','de','sfef','dfegre']
magicians_new = []

make_great(magicians_old[:],magicians_new)
show_magician(magicians_new)
show_magician(magicians_old)
