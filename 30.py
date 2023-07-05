'''
#BOJ 4101 크냐?

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

while True:
    a, b = map(int, input().split())

    if a==0 and b==0:
        break

    if a>b:
        print("Yes")
    else:
        print("No")