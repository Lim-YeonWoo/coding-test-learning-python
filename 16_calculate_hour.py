'''
#BOJ 2525 오븐 시계

[문제설명]
    시작 시각 : 14 30
    소요 시간 (분) : 20
    주어졌을때

    종료 시각 : 14 50 을 구해라

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

# 입력 받기
start_h, start_m = map(int, input().split())
time = int(input())

# 분 더해주기
temp = start_m + time

# 시간으로 바꿔주기
end_h = start_h + (temp//60)
end_m = temp%60

# 24시간 형식에 맞춰주기
if end_h >= 24:
    end_h = end_h - 24

print(end_h, end_m)
