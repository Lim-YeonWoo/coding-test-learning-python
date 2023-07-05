'''
#BOJ 2476 주사위 게임

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

n = int(input())

score = []

for i in range(n):
    a, b, c = map(int, input().split())

    if a==b and b==c:
        score.append(10000 + a*1000)
    elif a==b:
        score.append(1000 + a * 100)
    elif b==c:
        score.append(1000 + b * 100)
    elif a==c:
        score.append(1000 + c * 100)
    else:
        score.append(max(a,b,c)*100)

print(max(score))