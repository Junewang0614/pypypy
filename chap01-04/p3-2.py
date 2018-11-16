#打印人员名单
names = ['yhf','lb','lhq','xww']
print(names)

#删除一位嘉宾，并在相同位置加入一位嘉宾
popped_name = names.pop(1)
names.insert(1,'zym')

print(popped_name + " is too busy to come.")
print(names)

#替换一名嘉宾
print(names[0] + " refer to study,so he will not come.")
names[0] = 'lhy'
print(names)

#添加三名新嘉宾
names.insert(0,'jxg')
names.insert(2,'xm')
names.append('ww')

print(names)
print('\n')

#缩减嘉宾
message0 = 'Ther are only two people can have dinner with me.'
message1 = ",Let's have dinner,"
message2 = ",I'm sorry.There is no seat for you."

print(message0)

p1 = names.pop()
print(p1 + message2)
p2 = names.pop()
print(p2 + message2)
p3 = names.pop()
print(p3 + message2)
p4 = names.pop()
print(p4 + message2)
p5 = names.pop()
print(p5 + message2)
print('\n')

print(names)
print(names[0] + message1)
print(names[1] + message1)
print('\n')

del names[0]
del names[0]
print(names)








