# ABC50_A

# 文字列と数字の混合の入力
a, op, b = map(str,input().split())
if op == '+':
    print(int(a)+int(b))
else:
    print(int(a)-int(b))