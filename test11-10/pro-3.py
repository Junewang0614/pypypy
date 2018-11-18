list1 = []
n = input()

for i in range(int(n)):
    item = input()
    list1.append(item)

list1.reverse()
for item in list1:
    print(item)

print(len(list1))


