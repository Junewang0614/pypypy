nums = []
n = input()

for i in range(int(n)):
    num = input()
    nums.append(num)

sum0 = 0
for num in nums:
    m = len(num)
    num = int(num) // 10**(m-1)
    sum0 += num

print(sum0)




