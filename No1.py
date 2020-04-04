n = 0
a,b,c,d = input()
for i in [a,b,c,d]:
    if i == "+":
        n += 1
    else:
        n -= 1
print(n)