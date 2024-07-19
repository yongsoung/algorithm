input_num = int(input())
# voca = []
# for _ in range(input_num):
#     voca.append(list(input().strip()))

# count = 0
# for i in range(voca):
#     for j in range(len(voca[i])):
#         voca[i][j] == voca[i][j+1]
        
#         if group_voca =:
#         count += 1
count = input_num
for _ in range(input_num):
    voca = input()
    for i in range(len(voca)-1):
        if voca[i] == voca[i+1]:
            continue
        elif voca[i] in voca[i+1:]:
            count -=1
            break

print(count)