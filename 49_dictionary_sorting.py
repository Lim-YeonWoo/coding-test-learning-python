'''
#BOJ 11557 Yangjojang of The Year

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]
    dictionary를 sorting해서 풀었으나
    이렇게 최댓값만 구하면 되는 문제는 최댓값만 저장해서 푸는게 좋다.
'''

T = int(input())

for t in range(T):
    N = int(input())

    univ_dic = dict()
    for i in range(N):
        univ, score = input().split()
        univ_dic[univ] = int(score)

    result = sorted(univ_dic.items(), key=lambda x: x[1], reverse=True)
    print(result[0][0])
