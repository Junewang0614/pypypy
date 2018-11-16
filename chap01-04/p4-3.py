#使用切片打印前三个、中间三个、末尾三个元素

nums = list(range(1,21))

print('the first three items in the list are:')
print(nums[:3])
print('three items in the list are:')
print(nums[8:11])
print('the last three items in the list are:')
print(nums[-4:-1])
print('\t')

#创建列表副本
names = ['xiaoming','xiaohong','xiaofang']
names2 = names[:]

names.append('xiaolian')
names2.append('xiaohua')

for name1 in names:
    print(name1)
for name2 in names2:
    print(name2)
print('\t')


