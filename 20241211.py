# calendar 모듈
import calendar
calendar.prcal(2024)
calendar.prmonth(2024,12)
calendar.weekday(2024,8,12)
print(calendar.weekday(2024,12,15))  #월요일이 0이고 일요일이 6이라 6 출력


# 날짜로 요일 알아내기
import datetime

days = ["월", "화", "수", "목", "금", "토", "일"]
weekday = datetime.date.today().weekday()
print("오늘은 " + days[weekday] + "요일")

weekday = datetime.date(2024,12,25).weekday()
print("크리스마스는 " + days[weekday] + "요일")


# 날짜로 요일 알아내기 - 함수로 정의
import datetime

def get_weekday(yyyy, mm, dd):
    days = ["월", "화", "수", "목", "금", "토", "일"]
    weekday = datetime.date.today().weekday()
    print(f'{yyyy}년 {mm}월 {dd}일 {days[weekday]}요일')
get_weekday(2024,12,24)


# time 모듈 - time.time() -> 현재 시간을 초로 반환
import time
print(time.time())
time.sleep(2)  #2초 뒤에 밑에 print가 출력됨
print(time.time())

import time
a = time.time()
time.sleep(2)
b = time.time()
print(b-a)  #2로 출력됨


# time 모듈 - time.localtime() -> 년, 월, 일, 시, 분, 초로 반환
import time
print(time.localtime())
time_str = time.localtime()
print(time_str.tm_year)

# time 모듈 - time.ctime() -> 날짜와 시간 표기 형태
import time
print(time.ctime())
print(time.ctime(a))
print(time.ctime(b))

## 년과 일로 환산(1970.01.01 이후)
import time
year = time.time()/(365*24*60*60)
year_round = round(time.time()/(365*24*60*60))  #round는 소수점 반올림
print(year)
print(year_round)
day = time.time()/(24*60*60)
day_round = round(time.time()/(24*60*60))
print(day)
print(day_round)


# time 모듈 - 수행시간 측정하기
import time
start = time.time()

for i in range(10):
    print(i)
    time.sleep(1)

end = time.time()
print(f"수행시간 : {end-start}초")

## 함수화하기 -> 코드 전체 선택해서 control + . 누르고 method 누르면 함수로 바뀜
import time
def check_time(func):
    start = time.time()
    func()
    end = time.time()
    print(f"수행시간 : {end-start}초")

def a():
    for i in range(10):
        print(i)
        time.sleep(1)

def b():
    for i in range(100):
        print(i)
        time.sleep(0.5)

check_time(a)
check_time(b)


# sys 모듈
import sys
print(sys.argv)
args = sys.argv[1:]
print(args)  #이렇게 하고 터미널창에 python 파일명(20241211.py) 숫자입력 하면 입력값이 출력됨


# 연습문제1. 사용자가 입력한 모든 숫자를 더하는 프로그램을 만들어라(slack에 올라옴)
## 나의 방법
import sys
sum = 0
for i in range (1,len(sys.argv)):
    sum += int(sys.argv[i])
print(sum)

## 방법2.
import sys
args = sys.argv[1:]
sum = 0
for i in args:
    sum += int(i)
print(sum)


# 연습문제2. 세개를 입력받는데 mul이면 두 수를 곱하고 add면 두 수를 더해라(slack에 올라옴)
## 나의 방법
import sys
args = sys.argv[1:]
if len(args) <= 2 or len(args) >= 4:
    print("오류입니다")
else:
    if args[0] == "mul":
        print(int(args[1]) * int(args[2]))
    elif args[0] == "add":
        print(int(args[1]) + int(args[2]))

## 방법2
import sys
args = sys.argv
if (len(args)!=4):
    print("오류입니다")
else:
    cmd = args[1]
    num1 = int(args[2])
    num2 = int(args[3])
    if cmd == "mul":
        print(num1*num2)
    elif cmd == "add":
        print(num1+num2)


# sys 모듈 - sys.exit(0)
# 나의 방법
import sys
args = sys.argv[1:]
if len(args) <= 2 or len(args) >= 4:
    print("오류입니다")
    sys.exit(0)  #여기에 sys.exit(0)을 쓰면 밑에 else 안써도됨. 밑에 코드는 땡겨서 원칙대로 작성하기

if args[0] == "mul":
    print(int(args[1]) * int(args[2]))
elif args[0] == "add":
    print(int(args[1]) + int(args[2]))

## 방법2
import sys
args = sys.argv
if (len(args)!=4):
    print("오류입니다")
    sys.exit(0)  #여기에 sys.exit(0)을 쓰면 밑에 else 안써도됨. 밑에 코드는 땡겨서 원칙대로 작성하기
cmd = args[1]
num1 = int(args[2])
num2 = int(args[3])
if cmd == "mul":
        print(num1*num2)
elif cmd == "add":
        print(num1+num2)


# os 모듈
import os
os.chdir("C:/Users/soeun/codingon/python")  #현재 파일 위치(디렉터리 경로) 출력
dir = os.popen("git status")  #git status한 내용 출력(dir 명령으로 열기)
print(dir.read())  #디렉터리 보기(읽기)
dir = os.popen("dir")  #dir한 내용 출력
print(dir.read())


# 타자 연습 게임
import random
import time

word = ["sky", "earth", "moon", "flower", "tree", "apple", "grape", "garlic", "onion", "potato"]
n = 1  #문제번호

input("[타자 게임] 준비되면 엔터!")
start = time.time()  #시작시간

while n < 11:
    print("문제", n)
    question = random.choice(word)
    print(question)  #문제 출제
    user = input()
    if question == user:
        print("통과!!")
        n += 1
    else:
        print("오타! 다시 도전!")

end = time.time()  #종료시간
et = end - start
print(f"타자 시간 : {et: .2f}초")  #.2f는 et를 소수점 둘째자리까지 표시하겠다는 뜻(f:float 실수)


# 모듈 만들기 -> 다른 파일 만들어서 진행함(modules, modules2,mylib_user2)


# 파일 입출력 - w
f = open("text.txt", "w")  #text.txt 파일이 Python폴더안에 생성됨  #w는 파일에 데이터쓰기 위해서 여는데 기존 내용은 초기화된다
f.write("Hello World\n")
## print(f.write("Hello World\n"))  #Hello World 글자 수 출력(띄어쓰기 포함) : 12출력
f.close()


# 파일 입출력 - r(read)
f2 = open("text.txt")
print(f2.read())
f2.close()


# 파일 입출력 - a
f = open("text.txt", "a")  #text.txt 파일에 #1에 적은 내용이 추가됨
f.write("Hello World222\n")  #1
f.close()


# 파일 입출력 - readline()
f2 = open("text.txt")  
print(f2.read())
f2.close()

f3 = open("text.txt")
print(f3.readline(), end="")  #text.txt의 첫번째 줄 출력
print(f3.readline(), end="")  #text.txt의 두번째 줄 출력
print(f3.readline(), end="")  #text.txt의 세번째 줄 출력
f3.close()