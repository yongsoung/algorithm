string_a = input().strip()
string_b = input().strip()

def LCS(string_a, string_b):
    len_a = len(string_a)
    len_b = len(string_b)
    
    # 2차원 배열 초기화 (길이 + 1)
    dp = [[0] * (len_b + 1) for _ in range(len_a + 1)]
    
    for i in range(1, len_a + 1):
        for j in range(1, len_b + 1):
            if string_a[i - 1] == string_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[len_a][len_b]

print(LCS(string_a, string_b))
