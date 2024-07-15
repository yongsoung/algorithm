import sys

n = int(sys.stdin.readline())
height = list(map(int, sys.stdin.readline().split()))

## 스택 구현
height_index = [0] * n
stack = []

for i in range(n):
    
    while stack:
        if height[stack[-1][0]] < height[i]:
            stack.pop()
        else:
            height_index[i] = stack[-1][0] + 1
            break
    stack.append((i, height[i]))


print(*height_index)