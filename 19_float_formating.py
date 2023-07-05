'''
#BOJ 5355 화성 수학

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]
    *input이라는 변수명 쓰면 안됨

    *입력에 소수있을때 int()주의

    *소수 둘째자리까지 출력
        round(14.99,2)는 15.0 이 됨. 15.00  이 아니고.
        15.00으로 출력하려면 문자열 formating이 필요함.
        format() 이용.
        print( "{0}은 첫번째인자, {1}은 두번째인자 의미".format(첫인자, 두번째인자))
        print( "{0:.2f}".format(3.5555)) 는 3.56 출력
'''

T = int(input())

for i in range(T):
    op_list = input().split()

    for j, op in enumerate(op_list):
        if j == 0:
            res = float(op)
        else:
            if op == "@":
                res = res * 3
            elif op == "%":
                res = res + 5
            elif op == "#":
                res = res - 7

    print("{0:.2f}".format(res))
