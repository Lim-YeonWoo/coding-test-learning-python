'''
#BOJ 11021 A+B-7

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

T = int(input()) #테스트케이스 개수

for i in range(T):
    a, b = map(int, input().split())
    print(f"Case #{i+1}:", a+b)