'''
#BOJ 9498 시험 성적

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

score = int(input())

if 90<=score and score<=100:
    print("A")
elif 80<=score and score<=89:
    print("B")
elif 70<=score and score<=79:
    print("C")
elif 60<=score and score<=69:
    print("D")
else:
    print("F")
