num_coin, sum_coin = map(int, input().split())

coins = []
for _ in range(num_coin):
    coins.append(int(input()))

coins.sort(reverse=True)

def min_coin(coins, price):
    count = 0
    for coin in coins:
        if price == 0:
            break
        count += price // coin
        price %= coin
    return count

print(min_coin(coins, sum_coin))