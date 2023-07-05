'''
#BOJ 10988 팰린드롬인지 확인하기

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]

'''

word = input()
isPalindrome = True

for i in range(len(word)):
    if word[i] != word[len(word)-i-1]:
        isPalindrome=False

if isPalindrome:
    print("1")
else:
    print("0")