n = int(input())
a = list(map(int, input().split()))
a_min = 10**9
a_max = -10**9

for i in range(n):
    if a[i] < a_min:
        a_min = a[i]
    if a[i] > a_max:
        a_max = a[i]
print(a_min, a_max)