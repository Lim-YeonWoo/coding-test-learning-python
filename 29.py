'''
#BOJ 2480 주사위 세개

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]
    list에 3개 넣어서 sort할 필요없이
    a, b, c 받아서 max(a,b,c)해서 최댓값만 알았어도됨
'''

arr = list(map(int, input().split()))

arr.sort(reverse=True)

if arr[0]==arr[1]==arr[2]:
    print(10000+arr[0]*1000)
elif arr[0]==arr[1]:
    print(1000+arr[0]*100)
elif arr[1]==arr[2]:
    print(1000+arr[1]*100)
elif arr[0]==arr[2]:
    print(1000+arr[2]*100)
else:
    print(arr[0]*100)