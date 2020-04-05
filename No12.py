# ABC93_A
S = input()
list = ['a','b','c']
if S[0] in list:
    list.remove(S[0])
    if S[1] in list:
        list.remove(S[1])
        if S[2] in list:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')