print('The pastrami is sale out.')
sandwich_orders = ['zzy','zhz','pastrami','lc','zhb','pastrami','wyd','pastrami',]
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)


