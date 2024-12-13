# 바이너리 파일 읽고 쓰기 - 바이너리 파일
with open("./output/data.bin", "wb") as f:
    txt = "안녕"
    f.write(txt.encode())  #encode : 암호화

with open("./output/data.bin", "rb") as f:
    data = f.read()
    print(data)
    print(data.decode())  #decode : 복호화 -> 인코딩했으니까 디코딩 해야함(인코딩과 디코딩은 한 쌍)


# 바이너리 파일 읽고 쓰기 - 이미지 복사하기
with open("./output/maru.jpg", "rb") as f:
    img = f.read()

with open("./output/maru2.jpg", "wb") as f:
    f.write(img)


# 예외처리 예시
num = int(input("정수 입력"))  #정수가 아닌 수를 입력했을 때(ex.2.1) 에러 발생

try:  #try - except 구문을 이용해서 에러를 처리할 수 있다.
    num = int(input("숫자 입력"))
except ValueError:  #오류 내용
    print("정수가 아님! 정수를 입력해주세요!")

# 예외처리 예시 - as 에러
try:  #1
    num = int(input("정수 입력 : "))
except ValueError as msg:
    print(msg)

try:  #2 : #1과 같음(ValueError가 기억이 안날 때 걍 안적어도 예외처리할 수 있음)
    num = int(input("정수 입력 : "))
except:
    print("정수가 아님!")

try:  #3 : #1과 같은데 #2는 오류 메시지가 안뜨니까 메시지 뜨게 하고 싶으면 Exception 사용
    num = int(input("정수 입력 : "))
except Exception as msg:
    print(msg)


# 예외처리 에시 - 다중 예외처리
try:  
    num = int(input("정수 입력 : "))
except Exception as msg:  #에러 발생 시 즉시 점프하므로 Exception 출력
    print("Exception", msg)
except ValueError as msg:
    print("ValueError", msg)
else:
    print("예외 없음")

try:  
    num = int(input("정수 입력 : "))
except ValueError as msg:  #에러 발생 시 즉시 점프하므로 ValueError 출력
    print("ValueError", msg)
except Exception as msg:  
    print("Exception", msg)
else:
    print("예외 없음")


# 실습1. 정수 입력 받기
while True:
    try:
        num = int(input("숫자 입력: "))
        print(f"정수 입력 성공 : {num}")
        break
    except:
        print("정수가 아님! 정수를 입력해주세요!")


# 예외 처리 - try ~ except ~ finally 구문
while True:
    try:
        num = int(input("숫자 입력: "))
        print(f"정수 입력 성공 : {num}")
        break
    except:
        print("정수가 아님! 정수를 입력해주세요!")
    finally:  #finally 구문은 맞던 틀리던 반드시 실행됨(break를 했는데도 실행됨)
        print("무조건무조건이야")


# raise ~ Exception
## 리더님 예제
a = 1
try:
    a += 1
    raise Exception  #강제로 에러를 발생시켜서 밑에 a+=2와 print는 실행이 안됨
    a += 2
    print("a", a)
except:
    print("error", a)

## 강의자료 예제
class Animal:
    def breathe(self):
        print("숨을 쉰다")
    def cry(self):
        raise NotImplementedError  #NotImplementedError말고 Exception써도 되고 모든 다른 에러 사용 가능
    
class Dog(Animal):
    def cry(self):
        print("멍멍")

d = Dog()
d.breathe()
d.cry()