'''
#BOJ 3009 네 번째 점

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
    if y3 == y1:
        x4, y4 = x3, y2
    elif y3 == y2:
        x4, y4 = x3, y1

elif x2 == x3:
    if y1 == y2:
        x4, y4 = x1, y3
    elif y1 == y3:
        x4, y4 = x1, y2

elif x3 == x1:
    if y2 == y3:
        x4, y4 = x2, y1
    elif y2 == y1:
        x4, y4 = x2, y3

print(x4, y4)