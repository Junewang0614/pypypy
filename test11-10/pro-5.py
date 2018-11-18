ATGC = {'A':'U','T':'A','G':'C','C':'G',}
n = input()

k = ''
for i in str(n):
    j = ATGC[i]
    k = k + j 
print(k)
