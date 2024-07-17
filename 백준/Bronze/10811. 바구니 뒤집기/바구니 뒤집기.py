n, m = map(int, input().split())
basket = [i for i in range(1, n+1)]

for i in range(m):
    x, y = map(int, input().split())
    temp = basket[x-1: y]
    temp.reverse()
    basket[x-1: y] = temp

# temp = basket[2: 5]
# print(type(temp))
# temp.reverse()

# basket[2: 5] = temp
# print(basket)
print(" ".join(map(str, basket)))