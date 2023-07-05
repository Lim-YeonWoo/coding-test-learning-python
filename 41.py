'''
#BOJ 5086 배수와 약수

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

while True:
    a, b = map(int, input().split())

    if a==0 and b==0:
        break

    if a%b==0:
        print("multiple")
    elif b%a==0:
        print("factor")
    else:
        print("neither")
