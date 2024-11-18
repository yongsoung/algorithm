t = input()
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in t:
        print(t.index(i), end=' ')
    else:
        print(-1, end=' ')
