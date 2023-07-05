'''
#BOJ 10102 개표

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

n = int(input())

score = input()
a = score.count('A')
b = score.count('B')

if a>b:
    print('A')
elif a<b:
    print('B')
else:
    print('Tie')