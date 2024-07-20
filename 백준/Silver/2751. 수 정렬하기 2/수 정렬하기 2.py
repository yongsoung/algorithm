a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
b = sorted(b)
for i in range(len(b)):
    print(b[i])