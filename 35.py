'''
#BOJ 7567 그릇

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

bowl = input()

for i in range(len(bowl)):
    if i==0:
        cnt = 10 #cnt갱신
        before = bowl[i] #before갱신
    else:
        if before == bowl[i]:
            cnt = cnt + 5 #cnt갱신
            before = bowl[i]  # before갱신
        else:
            cnt = cnt + 10 #cnt갱신
            before = bowl[i] #before갱신
print(cnt)