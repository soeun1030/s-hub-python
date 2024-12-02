# 문자열 포맷 서식
print("오늘은 12월 %d일 입니다." %2)
print("오늘은 %d월 %d일 입니다." %(12,2))
print("오늘은 %d%s %d일 입니다." %(12, '월' ,2)) # 1,2,3번은 잘 사용하지 않음
print(f"오늘은 {12}{'월'} {2}일 입니다.") #이걸 제일 많이 사용
print("오늘은 " +str(12)+"월 "+str(2)+"일 입니다.")
print("오늘은 ",12,"월 ",2,"일 입니다.", sep="") #얘도 많이 사용

# 문자열 함수 - 대소문자로 변환 ## 코테에 많이 나옴
print("Hello".upper())
print("Hello".lower())


# 문자열 함수 - split() ## 매우 중요(반드시 암기)
friends = "고찬국 김다운 김민창"
a = friends.split() #띄어쓰기가 디폴트이므로 굳이 split(" ") 이렇게 띄어쓰기 안넣어도됨
print(a)

friends = "고찬국 김다운 김민창"
a = friends.split("김") #split안에 내가 쓴 거 기준으로 잘림 
print(a)


# 문자열 함수 - format()
sentence = "{}월 {}일".format(12,2) #{}안에 아무것도 없으면 순서대로 출력
print(sentence)

sentence = "{1}월 {0}일".format(12,2) #{}안에 쓴 순서대로 출력
print(sentence)


# 문자열 함수 - strip() : 앞뒤 공백 제거
b = "   111   222   "
print(b.strip())
print(b.split())

# 문자열 함수 - replacd() = control H


# 실습2
number1 = input()
number2 = input()

first = int(number1) * int(number2[2])
second = int(number1) * int(number2[1])
third = int(number1) * int(number2[0])
result = int(number1) * int(number2)

print(first)
print(second)
print(third)
print(result)

## 실습2 정답
in1 = int(input())
in2 = input()

print(in1*int(in2[2]))
print(in1*int(in2[1]))
print(in1*int(in2[0]))
print(in1*int(in2))


# # 비교 연산자
print(1==2)
print(1>2)
print(1<=2)

x = 2
print(1<x<3) # c언어 : (1<x && x>3)
print(True and False) # c언어 : &&
print(True or False) # c언어 : ||
print(not True) # print(!True)는 안됨 # c언어 : !


# in 연산자
cart = ["계란", "마늘", "콩나물", "커피"]
print("두부" in cart)
print("계란" in cart)


# if 조건문
if 1<3:
    print("True")
    print("True")
print("False") # if문이 True면 출력됨, 만약 False면 출력안되고 다음으로 넘어감


# 실습3
number = int(input())

if number%2 == 0:
    print("짝수")
if number%2 == 1:
    print("홀수")


if number%2 == 0: # else를 사용한 방법
    print("짝수")
else:
    print("홀수")


# 실습4
score = int(input())
if score>100:
    print("점수를 다시 입력하세요.")
elif score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("E")


# ## 실습4 정답
score = int(input())
if score>100:
    print("점수를 다시 입력하세요.")
elif score<60:
    print("E")
elif score<70:
    print("D")
elif score<80:
    print("C")
elif score<90:
    print("B")
else:
    print("A")


#실습5
age = int(input("나이를 숫자로 입력해 주세요 : "))
pay = input("결제 방법을 입력해주세요.('카드' 또는 '현금'만 입력)")
if age<8:
    print(f"{age}세의 {pay}요금은 무료입니다.")
elif age<14:
    print(f"{age}세의 {pay} 요금은 450원입니다.")
elif age<20:
    if pay == "카드":
        print(f"{age}세의 {pay} 요금은 720원입니다.")
    else:
        print(f"{age}세의 {pay} 요금은 1000원입니다.")
elif age<75:
    if pay == "카드":
        print(f"{age}세의 {pay} 요금은 1200원입니다.")
    else:
        print(f"{age}세의 {pay} 요금은 1300원입니다.")
else:
    print(f"{age}세의 {pay} 요금은 무료입니다.")

## 실습5 정답
age = int(input("나이를 숫자로 입력해 주세요 : "))
pay = input("결제 방법을 입력해주세요.('카드' 또는 '현금'만 입력)")
if age<8 or age>=75:
    money = "무료"
elif age<14:
    money = "450원"
elif age<20:
    if pay == "카드":
        money = "720원"
    else:
        money = "1000원"
elif age<75:
    if pay == "카드":
        money = "1200원"
    else:
        money = "1300원"

print(f"{age}세의 {pay} 요금은 {money}입니다.")