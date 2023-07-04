'''
#BOJ 10430 나머지

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

a, b, c = map(int, input().split())

print( (a+b)%c )
print( ((a%c) + (b%c)) % c)
print( (a*b)%c )
print( ((a%c) * (b%c)) % c )

