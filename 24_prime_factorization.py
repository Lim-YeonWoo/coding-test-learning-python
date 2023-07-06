'''
#BOJ 11653 소인수분해

[문제설명]
    정수 N이 주어졌을 때, 소인수분해하는 프로그램
[문제풀이]

[어려웠던 점 & 다시 공부할 부분]
    * [방법1] 에라토스테네스의 체 (sieve of Eratosthenes)
    : 소수를 대량으로 빠르고 정확하게 구하는 방법
    : 배열 이름이 sieve. sieve[x]=0이면 소수, 1이면 합성수.

    * [방법2] 2부터 나눠보기
    : 앞에서 i로 이미 최대한으로 나눴기 때문에 그냥 i+1로 갱신.
        n = int(input())
        i = 2
        while n!=1:
            if n%i == 0: #해당 i로 나눠질때까지 나누기
                print(i)
                n = n/i
            else:
                i+=1 #안되면 i증가
'''

n = int(input())

i = 2
while n!= 1:
    if n%i==0:
        print(i)
        n = n/i
    else:
        i += 1