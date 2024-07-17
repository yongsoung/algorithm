n, m = map(int, input().split())
basket = [[] for _ in range(n+1)]           # 빈 배열 만들기(0부터 n개)

for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i, j+1):
        basket[l].append(k)

for i in range(1, n+1):
    if basket[i] == []:
        print(0)
    else:
        print(basket[i][-1], end=' ')