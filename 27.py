'''
#BOJ 10039 평균 점수

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

sum = 0

for i in range(5):
    n = int(input())

    if n >= 40:
        sum = sum + n
    else:
        sum = sum + 40

print(int(sum/5))


