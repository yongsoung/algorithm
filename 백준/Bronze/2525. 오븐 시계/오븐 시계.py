a, b = map(int, input().split())
c = int(input())
result_b = (b + c) % 60
result_a = (a + (b + c) // 60) % 24
print(result_a, result_b)