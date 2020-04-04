# ABC122 B
S = input()
listS = list(S)
N = []
dic = ['A', 'T', 'G', 'C']
count = 0
for i in range(len(listS)):
    if listS[i] in dic:
        count += 1
        N.append(count)
    else:
        count = 0
        N.append(count)
print(max(N))