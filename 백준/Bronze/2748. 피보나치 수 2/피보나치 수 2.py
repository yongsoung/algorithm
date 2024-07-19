# 2748번 피보나치 -2(DP)

fibo = int(input())
# 1. 피보 <= 1 일때, 피보 1 값 설정
# 2. 피보값이 없을 때, dictionary 생성 - 조건체크
# 3. 
# 4. 피보(n) = 피보(n-1) + 피보(n-2)
# 5. 값 리턴 - 조건체크
# 6. 프린트

def fibo_top_down(fibo, memo = None):
    if memo is None:
        memo ={}

    if fibo in memo:
        return memo[fibo]

    if fibo <= 1:
        return fibo         
    memo[fibo] = fibo_top_down(fibo - 1, memo) + fibo_top_down(fibo - 2, memo)
    return memo[fibo]


print(fibo_top_down(fibo))