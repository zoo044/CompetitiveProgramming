# ABC126_A
N, K = map(int, input().split())
S = input()
listS = list(S)
listS[K-1] = listS[K-1].lower()
listS = ''.join(listS)
print(listS)