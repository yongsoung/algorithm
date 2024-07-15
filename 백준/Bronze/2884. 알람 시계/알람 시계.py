a, b = map(int, input().split())

if b >= 45:
    a, b = a, b-45
else:
    if a > 0:
        a, b = a-1, b+15
    else:
        a, b = a+23, b+15

print(a, b)