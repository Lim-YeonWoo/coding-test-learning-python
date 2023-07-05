'''
#BOJ 10156 과자

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

k, n, m = map(int, input().split())

res = k*n - m

if res >0:
    print(res)
else:
    print(0)