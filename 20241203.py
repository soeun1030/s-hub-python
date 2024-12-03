# while문
i=0
while i<5:
    i+=1
    print(i)
print("끝")


# 실습0. 1~10 중에 홀수만 출력
## 방법1
num=0 
while num<10:
    num+=1
    if num%2!=0:
        print(num)

## 방법2
num=1 
while num<10:
    print(num)
    num+=2
print("끝")


# 실습1. 1부터 사용자가 입력한 수까지 정수의 합 계산
## 방법1
num = int(input("어디까지 계산할까요?"))
sum1 = 0
sum2 = 0  #번외. 홀수의 합만 구하기
for i in range(1, num+1):
    sum1 += i
    if i % 2 != 0:
        sum2 += i
print(sum1) 
print(sum2)

# ## 방법2
num = int(input("어디까지 계산할까요?"))
sum1 = 0
sum2 = 0  #번외. 홀수의 합만 구하기
for i in range(1, num+1):
    sum1 += i
for i in range(1, num+2):
        sum2 += i
print(sum1) 
print(sum2)


# 실습2. 입력한 숫자만큼 카운트하고 "발사" 출력
num = int(input("몇 초?: "))
for i in range(num,0,-1):
     print(i, end=" ")
print("발사!!")


#실습3. 구구단 만들기
num = int(input("몇 단을 출력할까요? "))
for i in range(1,10):
    print(f"{num} * {i} = {num*i}")


# 내장함수 ex)sum
a = [10, 20, 30]
print(sum(a))  #1
print(sum(a)/len(a))

sum = 0  #2 -> #1과 똑같은 값 출력
for i in a:
    sum+=i
print(sum)


# for문 - 리스트 내포
a = [1, 2, 3, 4, 5]
a2 = []  #빈 리스트 생성
a3 = []
a4 = []

a3 = [i*3 for i in a]  #3의 배수
print(a3)

a4 = [i*3 for i in a if i%2==0]  #3의 배수이면서 짝수인 수
print(a4)


# 이중 for문
for y in range(3):
    for x in range(2):
        print(f"y: {y}, x: {x}")
    print()


# 이중 for문 - 구구단 전체
for i in range(2,10):
    print(f"[{i} 단]")
    for j in range(1,10):
        print(f"{i} x {j} = {i*j}")
    print()


# 이중 for문 - 자리 배치도 응용(고객수와 좌석행 입력받기)
print("*** 자리배치도 ***")
customer = int(input("고객수 입력: "))
row = int(input("좌석행 수 입력: "))

if customer % row == 0:
    column = customer // row
else:
    column = (customer // row) + 1  #기존 pdf에 있는 코드에서 여기까지 column과 row 자리만 바꾸면 됨

for i in range(0, row):
  for j in range(1, column + 1):
    seat = i * column + j
    if seat > customer:
      break
    print(seat, end=" ")
  print()


# 실습4. 별 찍기
num = int(input("몇 줄? >"))  #1번
for i in range(1, num+1):
    print("*"*i)

for i in range(1, num+1):  #2번
    print(" "*(num-i)+"*"*i)

for i in range(1, num+1):  #3번
    print(" "*(num-i)+"*"*(2*i-1))


# 실습5. 리스트 평균 구하기 ##slack에 올라온 정답과 확인해서 공부하기
num = input("숫자 여러 개 입력 > ").split()  #문제조건을 성립시키기 위해 split 사용하여 공백을 기준으로 문자열을 쪼개 리스트 생성
num = [int(n) for n in num]  #문자열을 int를 사용해 정수로 변환
print(num)

max = max(num)
min = min(num)
total = sum(num) - max - min
div = len(num) - 2

print(f"가장 큰 값: {max}")
print(f"가장 작은 값: {min}")

avg = total/div
print(f"나머지 값의 평균: {avg}")


# slack에 올라온(+사진찍어둔) map 한번 실제로 해보기