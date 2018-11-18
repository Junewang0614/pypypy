nums = []
nums2 = []
n = input()

for i in range(int(n)):
    num = input()
    nums.append(num)

for num in nums:
    m = len(str(num))
    num = num // 10**(m - 1)
    nums2.append(num)

print(sum(nums2))


