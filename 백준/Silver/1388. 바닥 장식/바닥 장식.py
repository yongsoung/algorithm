dec_height, dec_width = map(int, input().split())

floor_dec = []
for i in range(dec_height):
    a = list(input().strip())
    floor_dec.append(a)

size = dec_height * dec_width

# 가로줄 세기 (같은게 나오면 개수 카운트)
for i in range(dec_height):             # i = 세로줄 인덱스, j = 가로줄 인덱스
    j = 1
    while j < dec_width :
        if floor_dec[i][j] == floor_dec[i][j-1] == '-':         # 가로 모양이 '-'로 전에 모양과 같으면 사이즈 줄이기
            size -= 1
        j += 1
    

# 세로줄 세기
for j in range(dec_width):
    i = 1
    while i < dec_height:
        if floor_dec[i][j] == floor_dec[i-1][j] == '|':
            size -= 1
        i += 1


print(size)