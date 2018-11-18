DNA = {'A':'T','T':'A','G':'C','C':'G',}
counts = {}
n = input()

count1 = 0
count2 = 0

for i in str(n):
    j = DNA[i]
    if (i == 'A') or (j == 'A'):
        count1 += 1
    elif (i == 'C') or (j == 'C'):
        count2 += 1

counts['A'] = count1
counts['T'] = count1
counts['G'] = count2
counts['C'] = count2

print(counts)


    

