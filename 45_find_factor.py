'''
#BOJ 9506 약수들의 합

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

def find_divisor(n):
    divisor_list = []

    for i in range(1, int(n**(1/2)+1)):
        if n % i == 0:
            divisor_list.append(i)

            if ((i**2) != n): # 2*2 = 4 처럼 완전제곱 인게 아니라면
                divisor_list.append(n//i)
    divisor_list.sort()
    return divisor_list

while True:
    n = int(input())

    if n == -1:
        break

    divisor_list = find_divisor(n)
    divisor_list.remove(n)

    if n == sum(divisor_list):
        print(n, " = ", " + ".join(str(i) for i in divisor_list), sep="")
    else:
        print(n, "is NOT perfect.")

