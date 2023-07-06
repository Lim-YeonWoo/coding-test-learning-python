'''
#BOJ 10103 주사위 게임

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

T = int(input())

a_score = 100
b_score = 100
for t in range(T):
    a, b = map(int, input().split())

    if a<b:
        a_score = a_score - b
    elif a>b:
        b_score = b_score - a

print(a_score)
print(b_score)