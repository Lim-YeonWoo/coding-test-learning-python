'''
#BOJ 2530 인공지능 시계

[문제설명]
    시작 시각 : 14시 30분 0초
    소요 시간 : 200초
    주어졌을때

    종료 시각 : 14시 33분 20초
    를 구해라

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]
    *앞의 16번 문제의 변형문제인데 이 풀이가 더 깔끔한 것 같다.

    *파이썬 삼항 연산자
        [참일때] if [조건] else [거짓일때]

    *시간, 요일, 거스름돈처럼 0~n이 반복되는 수 => 모두 나머지연산으로 생각하기
        24시간제도 25나왔다고 -24 하는게 아니고 24로 나눈 나머지를 보는 것
'''

# 입력 받기
start_h, start_m, start_s = map(int, input().split())
time_s = int(input())

# 초 단위 계산
temp_s = start_s + time_s
end_s = temp_s%60

# 분 단위 계산
temp_m = start_m + (temp_s//60)
end_m = temp_m%60

# 시 단위 계산
temp_h = start_h + (temp_m//60)
end_h = temp_h % 24
'''
[24시간 변환]
    아래처럼 쓰면 틀린다. 
    end_h = (temp_h-24 if temp_h>=24 else temp_h) # 삼항연산자
    
    만약 60시간이 지났다면 시간이 61시 이렇게 되는데 거기서 24를 빼기만 하면 안된다.
    즉, 24시간도 나머지&몫이다.
'''

print(end_h, end_m, end_s)