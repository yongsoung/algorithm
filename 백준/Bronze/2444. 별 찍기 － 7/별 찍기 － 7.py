# 2444번 별 찍기 - 7
n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('*' * (2 * i - 1))

for j in range(1, n):
    print(' ' * (j), end='')
    print('*' * (2 * n - 1 - j * 2))
