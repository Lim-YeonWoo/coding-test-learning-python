'''
#BOJ 3046 R2

[문제설명]
    R1, R2 는 두 숫자
    S = (R1 + R2)/2 로 평균
    R1과 S를 알때 R2를 출력해라.
[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

R1, S = map(int, input().split())

R2 = S*2 - R1

print(R2)