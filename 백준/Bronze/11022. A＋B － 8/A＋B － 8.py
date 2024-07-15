t = int(input())  # 테스트 케이스 개수 t를 입력받음
for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a + b}')