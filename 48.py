'''
#BOJ 10214 Baseball

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

T = int(input())

y_score = 0
k_score = 0
for t in range(T):
    for i in range(9):
        y, k = map(int, input().split())
        y_score = y_score + y
        k_score = k_score + k

    if y_score>k_score:
        print("Yonsei")
    elif y_score<k_score:
        print("Korea")
    else:
        print("Draw")