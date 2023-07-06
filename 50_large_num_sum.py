'''
#BOJ 10757 큰 수 A+B

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]
    * c++로 풀 경우, long long 형을 초과한다.
    따라서 입력을 string으로 받고
    vector<int>에 넣어서
    덧셈계산기를 구현해야한다.

    * 파이썬의 경우, 아무리 큰 수여도 그냥 더하면 된다.
'''

a, b = map(int, input().split())
print(a+b)