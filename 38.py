'''
#BOJ 10886 0=not cute / 1=cute

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

n = int(input())

cnt0 = 0
cnt1 = 0

for i in range(n):
    a = int(input())

    if a == 0:
        cnt0 = cnt0 + 1
    else:
        cnt1 = cnt1 + 1

if cnt0>cnt1:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")