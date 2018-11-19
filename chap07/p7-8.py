sandwich_orders = ['zzy','zhz','lc','zhb','wyd']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)
    print('I made your tuna sandwich,' + sandwich)

print(sandwich_orders)
print(finished_sandwiches)
