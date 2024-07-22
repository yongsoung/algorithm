tile = int(input())

def tile_subsequence(tile):
    if tile <= 2:
        return tile

    dp = [0] * (tile + 1)               # 초기값 설정
    dp[1] = 1
    dp[2] = 2

    for i in range(3, tile + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

    return dp[tile]


print(tile_subsequence(tile))