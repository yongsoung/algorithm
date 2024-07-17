num = [0 for _ in range(10)]
rest = [0 for _ in range(10)]
for i in range(10):
    num[i] = int(input())
    rest[i] = num[i] % 42

result1 = set(rest)
print(len(result1))