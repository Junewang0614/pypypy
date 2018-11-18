counts = {}
n = input()

countA = 0
countG = 0


for i in str(n):
    if (i == 'A') or (i == 'T'):
        countA += 1
    elif (i == 'G') or (i == 'C'):
        countG += 1

counts['A'] = countA
counts['T'] = countA
counts['G'] = countG
counts['C'] = countG

print(counts)

