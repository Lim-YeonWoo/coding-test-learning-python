'''
#BOJ 10699 오늘 날짜

[문제설명]

[문제풀이]

[어려웠던 점 & 다시 공부할 부분]
    * 파이썬 오늘 날짜
    from datetime import datetime

    datetime.today() #현재날짜
    datetime.today().year #년
    datetime.today().month #월
    datetime.today().day #일
    datetime.today().hour #시간
    datetime.today().strftime("%Y%m%d%H%M%S") #YYYYmmddHHMMSS 형태로 출력

    * 파이썬 어제 날짜
    from datetime import datetime, timedelta

    yesterday = datetime.today() - timedelta(1)
'''

from datetime import datetime

print(datetime.today().strftime("%Y-%m-%d"))