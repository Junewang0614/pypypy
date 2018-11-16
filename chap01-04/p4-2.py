#打印1-20
for num in range(1,21):
    print(num)

#1-20总和
nums2 = list(range(1,21))
print(min(nums2))
print(str(max(nums2)))
print(str(sum(nums2)) + '\n')

#奇数
jishus = list(range(1,20,2))
for jishu in jishus:
    print(jishu)
print('\t')

#被三整除的数
zhengchus = list(range(3,31,3))
for zhengchu in zhengchus:
    print(zhengchu)
print('\t')

#打印立方
lifangs = []
for num in range(1,11):
    lifang = num**3
    lifangs.append(lifang)
print(lifangs)
print('\t')

#用列表解析生成立方列表
lifangs2 = [num**3 for num in range(1,11)]
for lifang in lifangs2:
    print(lifang)



