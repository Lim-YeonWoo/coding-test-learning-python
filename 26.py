'''
#BOJ 2753 윤년

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

n = int(input())

if n%4==0 and n%100!=0:
    print('1')
elif n%400==0:
    print('1')
else:
    print('0')