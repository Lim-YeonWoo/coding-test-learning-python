'''
#BOJ 10162 전자레인지

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

time = int(input())

a = time // (5*60)
time = time % (5*60)

b = time // 60
time = time % 60

c = time // 10
time = time % 10

if time==0:
    print(a, b, c)
else:
    print(-1)

