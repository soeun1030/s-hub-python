# 2차원 리스트를 이용하여 구구단 3단 출력하기
d = [
    [3, 1],
    [3, 2],
    [3, 3],
    [3, 4],
    [3, 5],
    [3, 6],
    [3, 7],
    [3, 8],
    [3, 9]
]

for x, y in d:  #방법1
    print(f"{x} x {y} = {x*y}")

for i in d:  #방법2
    print(f"{i[0]} x {i[1]} = {i[0]*i[1]}")

for i in range(len(d)):  #방법3
    print(f"{d[i][0]} x {d[i][1]} = {d[1][0]*d[i][1]}")


# 함수
def f(x):
    result = x**2 + 2*x + 1
    return result
print(f(3))


# 함수 기본 구조
def sayHi():
    print("Hi")
    print("Hi")
    print("Hi")
sayHi()


# 변수 범위
x = 10  #전역변수
def func():
    x = 20  #지역변수
    print(x)
func()
print(x)

def func2():
    print("func2", x)
def func():
    x = 20
    y = 11
    print("func", x, y)
    func2()
func()
print("main", x)
func2()

def func3(x):
    print("func3", x)
func3(3)


# 실습1
## 방법1
def number(n1, n2):
    if n1 == n2:
        print(f"결과(곱): {n1*n2}")
    else:
        print(f"결과(합): {n1+n2}")
number(2,2)
number(2,3)

## 방법2
def data(x, y):
    if x==y:
        return x * y
    else:
        return x + y
value1 = data(2, 2)
print(f"결과(곱): {value1}")
value2 = data(2,3)
print(f"결과(합): {value2}")


# 실습2 - 입력값은(개당가격, 수량)
## 방법1
def total(money, amount):
    total_price = money*amount
    if total_price < 20000:
        return total_price + 2500
    else:
        return total_price
value1 = total(4000, 4)
print(f"상품1 가격: {value1}원")
value2 = total(4000, 5)
print(f"상품2 가격: {value2}원")

## 방법2
def total(가격, 수량):
    total_price = 가격 * 수량
    fee = 2500
    if total_price < 20000:
        total_price += fee
    return total_price
print(f"상품1 가격: {total(4000, 4)}원")
print(f"상품1 가격: {total(4000, 5)}원")


# 매개변수로 리스트(배열) 전달
def times (l):
    l2 = [i*2 for i in l]
    return l2

v2 = times([1,2,3,4,5])
print(v2)

# 파이썬은 2개 리턴도 가능(c언어는 불가)
def sum_mul(a, b):
    sum = a+b
    mul = a*b
    return sum, mul  #이 부분에서 2개 리턴 가능

s, m = sum_mul(2,3)
print(s,m)


# 실습3. 자판기 프로그램 함수화
## slack에 올려준 코드보고 혼자 다시해보기


# 실습4. 함수 & 스택(리스트)
import sys

stack = []
num = int(sys.stdin.readline())

def push(x):
    stack.append(x)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

for i in range(num):  #1
    a = sys.stdin.readline().split()
    if a[0] == "push":
        push(a[1])
    elif a[0] == "pop":
        pop()
    elif a[0] == "size":
        size()
    elif a[0] == "empty":
        empty()
    elif a[0] == "top":
        top()

# match case 해보기
## 바로 위의 1 대신 이거 넣으면 됨
for i in range(num):
    a = sys.stdin.readline().split()
    match a[0]:
        case 'push':
            push(a[1])
        case 'pop':
            pop()
        case 'size':
            size()
        case 'empty':
            empty()
        case 'top':
            top()


# 변수의 유효 범위
def oneUp():
    global x
    x = x+1
    return x
x = 0
print(oneUp())
print(oneUp())
print(oneUp())


# 실습5
def get_times(n):
    global count
    for i in range(1,31):
        if i % n == 0:
            print(i,end=" ")
            count += 1
count = 0
n = 3
get_times(n)
print(f"\n{n}의 배수의 개수: {count}")