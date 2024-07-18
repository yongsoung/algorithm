# 새로 구한 평균 : {최대값 + a / 최대값 * 100 + b / 최대값 * 100 } /3

subject_num = int(input())
test_score = list(map(int, input().split()))

test_score.sort()

print((sum(test_score)/ test_score[-1] * 100) / subject_num)