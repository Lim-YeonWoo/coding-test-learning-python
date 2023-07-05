'''
#BOJ 8958 OX퀴즈

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

T = int(input())

for t in range(T):
    score_list = input()

    cnt = 0
    res = 0
    for i,score in enumerate(score_list):
        if score == 'O':
            cnt = cnt + 1 #cnt 갱신
            res = res + cnt  # res 갱신
        else:
            cnt = 0 #cnt 갱신

    print(res)

