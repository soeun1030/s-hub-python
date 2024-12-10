# 실습2. Supermarket 클래스
class Supermarket:
    count = 0
    def __init__(self, location, name, product, customer):
        self.__location = location
        self.__name = name
        self.__product = product
        self.__customer = customer
        Supermarket.count += 1

    def print_location(self):
        print (f"위치 : {self.__location}")
    
    def change_category(self, new_product):
        self.__product = new_product
        print (f"파는 물건이 {new_product}로 바뀌었습니다.")
    
    def show_list(self):
        print (f"현재 파는 물건 : {self.__product}")
    
    def enter_customer(self):
        self.__customer += 1
        print (f"현재 있는 손님 수 : {self.__customer}")
    
    def show_info(self):
        print (f"가게 이름 : {self.__name}, 위치 : {self.__location}, 파는 물건 : {self.__product}, 손님 수 : {self.__customer}")
    
    def show_supermarket_count(self):  #여기에 self빼면
        print (f"슈퍼마켓 인스턴스 개수 : {Supermarket.count}")
    
a = Supermarket("포항", "고굽남", "삼겹살", 10)
b = Supermarket("홍대", "바다회사랑", "회", 15)

a.print_location()
a.change_category("된장찌개")
a.show_list()
a.enter_customer()
a.show_info()
a.show_supermarket_count()  #여기랑


b.show_info()
b.show_supermarket_count()  #여기에서 a.b.말고 Supermarket.으로 해야한다


# 클래스 상속
class Country:  #parent 클래스
    def __init__(self):
        self.name = "나라이름"
        self.population = "인구"
        self.capital = "수도"

    def show(self):
        print("국가 클래스의 메소드")

class Korea(Country):  #child 클래스
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("국가 이름은 :", self.name)

country = Korea("대한민국")
country.show()
print(country.name)
country.show_name()


# 메서드 오버라이딩
class Country:  #parent 클래스
    def __init__(self):
        self.name = "나라이름"
        self.population = "인구"
        self.capital = "수도"

    def show(self):
        print("국가 클래스의 메소드")

class Korea(Country):  #child 클래스
    def __init__(self, name):
        self.name = name

    def show(self):  #이걸 show로 바꾸면 오버라이딩됨 -> 국가 클래스의 메소드 내용 출력안됨
        print("국가 이름은 :", self.name)

country = Korea("대한민국")
country.show()
print(country.name)
# country.show_name()


# 실습3.
class Calculator():
    def __init__(self):
        self.value = 100  #초기 value 값 설정

    def sub(self, value):
        self.value -= value  #기본적으로 value 감소시킴

class MinLimitCalculator(Calculator):
    def sub(self, value):  #부모 클래스의 sub 메서드 호출
        self.value -= value
        if self.value < 0:  #value가 음수가 되지 않도록 설정
            self.value = 0
        # self.value = max(0, self.value-value)  #if문 대신 사용가능
        # super().sub(value)  #if문 대신 이 두줄도 사용 가능
        # self.value = max(0, self.value)

cal = MinLimitCalculator()
cal.sub(20)  #100-20 = 80
cal.sub(90)  #80-90 = -10 -> 0 출력
print(cal.value)


# 오버로딩
class Calculator():
    def __init__(self):
        self.value = 100

    def sub(self, value):
        self.value -= value

    # def sub(self):  #메소드 오버로딩(파이썬은 안됨, c언어만 가능)
    #     self.value -= 10

    # def sub(self, value1, value2):  #메소드 오버로딩(파이썬은 안됨, c언어만 가능)
    #     self.value = value1 - value2

    def sub(self, *args):  #오버로딩하고싶으면 이 방법 사용
        self.value = args[0]

a = Calculator()
a.sub(10)
print(a.value)


# 모듈 만들고 불러오기
# 모듈 불러오기 방법1
import calc_module  #컨트롤누르고 초록색(파일이름) 클릭하면 파일나타남
print(calc_module.add(1,2))  #파일이름쓰고 점누르면 파일의 기능이 뜬다
print(calc_module.div(1,2))
print(calc_module.mul(1,2))
print(calc_module.sub(1,2))

## 모듈 불러오기 방법2
from calc_module import add
print(add(1,2))  #calc_module.add()는 안됨

## 모듈 불러오기 방법3
import calc_module as cm  #calc_module을 cm으로 줄이고 계속 cm으로 사용하는 방법
print(cm.add(1,2))


# 표준모듈 - math 모듈
## 방법1
import math
print(math.floor(3.141592))  #내림
print(math.ceil(3.141592))  #올림
print(math.sqrt(9))  #9의 제곱근

## 방법2
from math import floor, ceil, sqrt
print(floor(3.141592))
print(ceil(3.141592))
print(sqrt(9))


# 표준모듈 - random 모듈
import random
print(random.randint(1,5))  #1,5 포함
print(random.uniform(1,2))  #1,2 포함
print(random.random())  #0부터 1사이의 임의의 실수
print(random.randrange(1,5))  #5 미포함
print(random.randrange(1,5,2))  #1,3만 출력, 5 미포함


# up_and_down 게임
# 나의 방법(10번일 때 break가 없어 틀림)
import random

com = random.randint(1,100)

min_v = 1  #최소값
max_v = 100
count = 0
score = 110

while True:
    try:
        count += 1
        score -= 10
        guess = int(input("숫자 입력(%d ~ %d): " % (min_v,max_v)))
        if guess < 0 or guess > 100:
            print("입력 범위를 초과했어요")
        elif com == guess:
            print("정답이에요!!")
            print(f"정답 : {com}")
            print(f"횟수 : {count}회")
            print(f"점수 : {score}점")
            break
        elif com > guess:
            print("랜덤수보다 작아요")
            min_v = guess
        else:
            print("랜덤수보다 커요")
            max_v = guess
    except ValueError:
        print("숫자만 입력 가능합니다.")

## 풀이
import random

com = random.randint(1,100)

min_v = 1  #최소값
max_v = 100

for i in range(10):
    try:
        guess = int(input("숫자 입력(%d ~ %d): " % (min_v,max_v)))
        if guess < min_v or guess > max_v:
            print("입력 범위를 초과했어요")
        elif com == guess:
            print("정답이에요!!")
            break
        elif com > guess:
            print("랜덤수보다 작아요")
            min_v = guess
        else:
            print("랜덤수보다 커요")
            max_v = guess
    except ValueError:
        print("숫자만 입력 가능합니다.")

print(f"정답 : {guess}")
print(f"점수 : {(10-i) * 10}점")


# 실습. 로또 번호 뽑기
## 방법1
import random
lotto = []
while len(lotto)<6:  #6개가 뽑힐 때까지 반복
    num = random.randint(1,45)
    if num not in lotto:
        lotto.append(num)
lotto.sort()
print(f"로또 번호 : {lotto}")  #print(sorted(lotto))

## 방법2 - set(집합)d으로 구현하기
lotto = set()
while True:
    x = random.randint(1,45)
    lotto.add(x)
    if len(lotto) == 6:
        break
sorted_lotto = sorted(lotto)  #set은 sort()안됨, sorted() 이용해서 새로운 리스트로 정렬하기
print(sorted_lotto)

## 방법3 - sample 사용
lotto = random.sample(range(1,46),6)
print(sorted(lotto))


# datetiem 모듈 - datetime.datetime
import datetime
now = datetime.datetime.today()
print(now)  #현재 날짜와 시간
print(now.year)  #현재 년도
print(now.month)  #현재 월
print(now.day)  #현재 일
print(f"{now.hour}시 {now.minute}분 {now.second}초")


# datetiem 모듈 - datetime.date
import datetime
today = datetime.date.today()
print(today)
# print(today.hour) datetime.date는 날짜만 물어본거라 hour해도 안됨


# datetime 모듈 - 지나온 날짜 계산하기
import datetime

print("지금까지 몇 일?")
first_day = datetime.date(2024, 11, 25)
print(first_day)

today = datetime.date.today()
print(today)

passed_time = today - first_day
print(passed_time)

print(f"개강 이후 {passed_time.days}일 지났습니다.")