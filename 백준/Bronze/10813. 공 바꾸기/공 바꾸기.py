n, m = map(int, input().split())
basket = [a for a in range(1, n+1)]
     # 배열 안에 인덱스 값 넣기

for a in range(m):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]

# for k in range(n):
#     print(basket[k], end=' ')

for k in basket:
    print(k, end=' ')