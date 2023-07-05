'''
#BOJ 5063 TGN

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

T = int(input())

for t in range(T):
    r, e, c = map(int, input().split())

    if r < (e-c):
        print("advertise")
    elif r==(e-c):
        print("does not matter")
    else:
        print("do not advertise")