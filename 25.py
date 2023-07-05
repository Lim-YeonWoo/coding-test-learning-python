'''
#BOJ 1789 수들의 합

[문제설명]
    서로 다른 N개의 자연수의 합이 S라고 한다.
    S를 알 때, 자연수 N의 최댓값은 얼마일까?
[문제풀이]
    1+2+3...을 해보다가 이 값이 S랑 같아지면 그 개수를,
    이 값이 S보다 커져버리면 개수는 -1해서 그대로 유지하고 뒷숫자애들을 변경해주면 된다.
    ex) 20이면 1+2+3+4+5까진 15로 ok.
        1+2+3+4+5+6=21이므로 1+2+3+4+5로 유지하고 5를 10으로 바꾸면된다.
[어려웠던 점 & 다시 공부할 부분]

'''

S = int(input())

i = 1
cnt = 0
temp = 0
while True:
    if temp == S:
        print(cnt)
        break
    elif temp > S:
        print(cnt-1)
        break
    else:
        temp = temp + i #temp갱신
        i =  i + 1 #i++
        cnt = cnt + 1 #cnt++