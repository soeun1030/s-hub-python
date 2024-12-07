# 함수의 기본 매개변수
def pr_str(txt, count=1):  #txt, count 순서가 이렇게 되면 오류 -> 반드시 디폴트가 앞에 있어야함
    for i in range(count):
        print(txt)

pr_str("Hello", 3)
print()
pr_str("Hello")
print()

def pr_str(txt, count=1, count2=1):
    for i in range(count):
        print(txt)
        print(count2)

pr_str("Hello", 3, 2)
pr_str("Hello", 3)
print()
pr_str("Hello")
print()  #위에 def pr_str(txt="12", count=1, count2=1): 이렇게 넣으면 마지막에 pr_str() 얘를 추가해줘야 12 출력됨 


# 함수의 가변 매개변수 - 가변 매개변수
def calc_avg(*numbers):  #만약 여기 *를 안쓰는 경우
    print(type(numbers))
    return sum(numbers)/len(numbers)

print(calc_avg(1,2))  #여기에서 print(calc_avg((1,2))) 이렇게 print할 때 튜플 사용하기
print(calc_avg(1,2,3,4,5))

def a():
    return 1,2
print(a())


# 함수의 가변 매개변수 - 가변 키워드 매개변수  #많이 안쓰임
def intro(**kw):  #intro = introduce
    print(type(kw))
    for k, v in kw.items():
        print(f"{k}: {v}")
    for i in kw:
        print(f"{i}")

intro(name="Alice", age=25, city="NY")

def a(*numbers, b):
    print(numbers, "b", b)
a(1,2,3,4,b=5)  #a(1,2,3,4,5) 얘는 에러


# 내장 함수 - sorted()
list = [2,4,1,4,6]
list.sort()  #원본 변환
print("list", list)

list2 = [2,4,1,4,6]
print("sorted list2", sorted(list2))  #원본 변환 x  #리턴값이 list다
print("list2", list2)


# 3번째로 작은 값의 인덱스를 구하라. -> 정렬하고 그 값을 원본에서 찾기 -> sort 쓰면 원본이 날라가기 때문에 sorted 사용하기
list = [2,4,1,5,6]
print(sorted(list)[2])


# 내장함수 - eval(evaluation)
print(eval("1+2"))
print(eval("1+2*2"))


# 내장함수 - round(반올림)
print(round(4.6))  #파이썬은 가장 가까운 짝수로 반올림하므로 4.5는 4로 나오고 5.5는 6으로 나옴. 반드시 주의할 것
print(round(4.4))

print(int(4.6+0.5))  #함수 굳이 안쓰고 간단하게 반올림하는 방법
print(int(4.4+0.5))

print(round(2.547))
print(round(2.547, 1))  #소수점 첫째자리에서 반올림
print(round(2.547, 2))  #소수점 둘째자리에서 반올림
print(round(127, -1))  #첫째자리에서 반올림
print(round(127, -2))  #둘째자리에서 반올림


# 내장함수 - pow(거듭제곱)
print(2**3)
print(pow(2,3))


# 내장함수 - list(s)
l = ["p","y","t","h","o","n"]
print("".join(l))


# 재귀함수 ##반드시 종료조건이 필요함 ###중요
def hello():  
    print("Hello, World!")
    hello()
hello()  #이 코드는 종료조건이 없으므로 무한반복되어 에러

def hello():
    global count  #종료조건
    count += 1
    if count<4:
        print("Hello, World!")
        hello()
count=0
hello()  #자기 자신 호출


# 팩토리얼
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))


# 실습2. 재귀함수로 피보나치 수 구하기
num = int(input("수를 입력하시오: "))
def fibo(n):
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)
print(fibo(num))

for i in range(num):  #순서대로 내역 모두 출력
    print(fibo(i), end = " ")

# 실습2를 최적화시키기 ##memoization 사용
num = int(input("수를 입력하시오: "))
memory = {1: 1, 2: 1}
def fibo_memo(n):
    if n in memory:
        result = memory[n]
    else:
        result = fibo_memo(n-1) + fibo_memo(n-2)
        memory[n] = result
    return result
print(fibo_memo(num))


# 하노이의 탑 코드 - 재귀함수에서 유명한 내용  ##fn = fn-1 + 1 + fn-1
num = int(input("수를 입력하시오: "))
total_moves = 0
def hanoi(number_of_disks_to_move, from_, to_, via_):
    global total_moves
    if number_of_disks_to_move == 1:
        print(from_, "->", to_)
        total_moves += 1
    else:
        hanoi(number_of_disks_to_move-1, from_, via_, to_)
        print(from_, "->", to_)
        total_moves += 1
        hanoi(number_of_disks_to_move-1, via_, to_, from_)
print(hanoi(num, "A", "c", "b"))
print("총 이동 횟수: ", total_moves)


# 람다식(Lambda Expresiions)
add = lambda x,y:x+y  #함수를 변수에 넣을 수 있음  #1
print(type(add))
print(add(1,2))

def add2(x,y):  #1과 같음
    return x+y
add3 = add2
print(add2(1,2))
print(add3(1,2))


# 람다함수를 매개변수로 전달하기
def call_3(func):
    for _ in range(3):
        func()
call_3(lambda:print("hi"))  #호출


# 람다식 - download
def download(startedCallback, endedCallback):
    startedCallback()
    endedCallback()
download(lambda:print("다운로드를 시작합니다."),lambda:print("완료되었습니다."))


# 람다식 - map()함수와 함께 사용
list(map(int, ["1","2","3"]))
result = map(lambda x:3*x, [1,2,3,4])
print(list(result))


# 람다식 - filter()함수와 함께 사용
li = [-5,1,2,-11,76]
value = list(filter(lambda x:x<0, li))
print(value)
value = list(filter(lambda x:x>10, li))
print(value)


# 연습문제. 위의 li를 2배한 후 3이상인 수만 한줄로 출력하기
print(list(filter(lambda x:x>=3, map(lambda x:2*x, li))))


# 연습1. 조건에 맞게 수열 변환하기1(프로그래머스 문제)
# https://school.programmers.co.kr/learn/courses/30/lessons/181882
def solution(arr):
    answer = []
    for i in arr:
        if i>=50 and i%2 == 0:
            answer.append(i/2)
        elif i<50 and i%2 != 0:
            answer.append(2*i)
        else:
            answer.append(i)
    return answer


# 연습2. x 사이의 개수(프로그래머스 문제)
# https://school.programmers.co.kr/learn/courses/30/lessons/181867
def solution(myString):
    answer = []
    a = myString.split("x")
    for i in a:
        answer.append(len(i))
    return answer


# 연습3. 부분 문자열(프로그래머스 문제)
# https://school.programmers.co.kr/learn/courses/30/lessons/181842
def solution(str1, str2):
    if str1 in str2:
        return 1
    else:
        return 0
    

#####집가서 연습1-3 입력받고 출력하는거 해보기