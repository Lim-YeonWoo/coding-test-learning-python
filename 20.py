'''
#BOJ 2675 문자열 반복

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

T = int(input())

for t in range(T):
    input_list = input().split()

    n = int(input_list[0])
    string = input_list[1]

    res = ""
    for i, char in enumerate(string):
        res = res + (char*n)

    print(res)