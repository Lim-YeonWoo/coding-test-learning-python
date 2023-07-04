'''
#BOJ 2588 곱셈

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]
    정수는 indexing불가능 (a=123 a[2]와 같이 접근 불가)
    문자열로 바꾼 후 indexing & slicing 하고 다시 int()로 바꾸자.
'''

input1 = input() #일부러 int()로 안바꿈
input2 = input()

res3 = int(input1) * int(input2[2])
res4 = int(input1) * int(input2[1])
res5 = int(input1) * int(input2[0])
res6 = int(input1) * int(input2)

print(res3)
print(res4)
print(res5)
print(res6)