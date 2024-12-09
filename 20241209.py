# 클래스 선언
a = dict()  #dict 자체가 클래스다
a = set()  #set 자체가 클래스다

class b:  #붕어빵 틀
    pass  

bb1 = b()  #붕어빵1
bb2 = b()  #붕어빵2
bb3 = b()  #붕어빵3


# 클래스 변수
class Movie:
    title = "범죄도시4"
movie1 = Movie()
movie2 = Movie()

print(movie1.title)
print(movie2.title)

movie1.title = "파묘"  #붕어빵끼리는 서로 관여안시키기 때문에 1을 바꿔도 2는 바뀌지 않는다.
print(movie1.title)  #따라서 얘는 파묘가 출력되고
print(movie2.title)  #얘는 그대로 범죄도시 출력

movie1.score = "1"
print(movie1.score)  #1로 출력  
print(movie2.score)  #movie2.score를 안만들었으니 에러


# 클래스 함수
class Movie:
    name = ''
    def print_msg(msg):
        print(msg)
    def modify(self,movie):
        self.name = movie
    def print_name(self):
        print(self.name)

movie1 = Movie()
movie2 = Movie()

Movie.print_msg("print하기")
# movie1.print_msg("ttt")  #self가 자동을 들어가있기에 에러

movie1.modify("프린트하기2")  #self랑 movie 모두 위에서 썼지만 movie만 쓰는 이유 : self는 자동으로 들어가기 때문 -> 객체를 사용할 땐 self 적으면 안됨
# Movie.modify(movie1, "print하기2")  #이 방법은 잘 안씀  #class를 사용할 땐 self를 반드시 적어야함
movie1.print_name()  #print하는 방법1

movie2.modify("프린트하기3")
print("movie2.name", movie2.name)  #print하는 방법2


# 생성자
class Movie:
    def __init__(self):
        print("Hello")
movie = Movie()


# 매개변수가 있는 생성자
class Movie:
    count = 0  #여기선 아무 의미 없는 코드(안적어도됨)
    def __init__(self, title, audience):  #1
    # def __init__(self, title="오징어게임", audience=300):  #2
        self.title = title
        self.audience = audience
movie1 = Movie("파묘", 100)
movie2 = Movie("파묘2", 200)

print(movie1.title, movie1.audience)
print(movie2.title, movie2.audience)

movie3 = Movie()  #매개변수가 있는 생성자이므로 얘 있으면 에러  #얘를 사용하고 싶으면 1에 2처럼 작성하기
print(movie3.title, movie3.audience)


# 클래스 변수 vs 인스턴스 변수
class Movie:
    count = 0  
    def __init__(self, title, audience):  
        self.title = title
        self.audience = audience
        Movie.count += 1  #클래스 변수 - 붕어빵틀을 바꿨으므로 movie1,2 모두 1씩 추가됨
movie1 = Movie("파묘", 100)
print(Movie.count)  #1
movie2 = Movie("파묘2", 200)
print(movie1.count)  #2
print(movie2.count)  #2
print(Movie.count)  #2

Movie.count += 1  #클래스 변수
print(movie1.count)  #3
print(movie2.count)  #3
print(Movie.count)  #3

movie1.count += 1    #인스턴스 변수  #붕어빵만 바꾼거이므로 movie1만 1추가됨
print(movie1.count)  #4
print(movie2.count)  #3
print(Movie.count)  #3

Movie.count += 1  #클래스 변수 -> 바로 위에서 movie1값은 4였지만 클래스 변수를 이용하면 다 같은 값으로 바뀜
print(movie1.count)  #따라서 4로 출력
print(movie2.count)  #4
print(Movie.count)  #4


# 접근제어
class Movie:
    count = 0  
    def __init__(self, title, audience):  
        self.__title = title  #private
        self._audience = audience  #protected
        Movie.count += 1

    def set_title(self,title):  #self.__title은 외부에서 접근하지 못하므로 본인만 바꿀 수 있게 set을 이용하여 함수 생성
        self.__title = title

    def get_title(self):  #set에서 생성하고 수정한 내용을 외부도 볼수있게 하기 이해 get을 사용하여 반환
        return self.__title

    def get_audience(self):
        return self._audience
    
movie1 = Movie("파묘", 100)
print(movie1.get_title())
# print(movie1.__title)  #private하므로 이렇게 작성하면 에러

print(movie1.get_audience())
print(movie1._audience)  #얘는 에러 안뜸

movie1.set_title("타이타닉")  #movie1 내용 바꾸고 싶으면 이렇게 작성하기
print(movie1.get_title())


# 연습1. slack에 올라옴(메소드 구현)
class MyAdd:
    __a = 1
    __b = 2

    def sum(self):  #sum은 위에서 사용한 get_title과 같음. 그냥 내가 함수 이름을 지정하는거
        return self.__a + self.__b
    
    def set_x(self, a):  #set_x는 위에서 사용한 set_title과 같음. 얘도 그냥 내가 함수 지정하는거
        self.__a = a

a = MyAdd()
print(a.sum())  
a.set_x(3)  # __a 값 3으로 변경 #a.__a = 3 이건 에러
print(a.sum())  


# 정보 은닉
class Health:
    def __init__(self, name):  #만약 여기에 self, name, hp하면
        self.__name = name
        self.__hp = 100  # 여기에 self.__hp = hp 하고

    def get_name(self):
        return self.__name
    
    def set_hp(self, hp):
        hp = max(hp, 0)
        hp = min(hp, 100)
        # if hp < 0:  #이렇게 해도 됨
        #     hp = 0
        # elif hp > 100:
        #     hp = 100
        self.__hp = hp

    def get_hp_str(self):
        return "hp: " + str(self.__hp)
    
    def exercise(self, hours):
        self.set_hp(self.__hp + hours)
        print(f"{hours}시간 운동하다")

    def drink(self, cups):
        self.set_hp(self.__hp - cups)
        print(f"술을 {cups}잔 마시다")

p1 = Health("나몸짱")  #여기에 Health("나몸짱", 100) 하면됨
p1.set_hp(100)
p1.exercise(5)
p1.drink(2)
print(f"{p1.get_name()} - {p1.get_hp_str()}")

p2 = Health("나약해")
p2.set_hp(10)
p2.exercise(1)
p2.drink(12)
print(f"{p2.get_name()} - {p2.get_hp_str()}")


# 실습1. 사칙연산 클래스 만들기
class Calculate:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def set_cal(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def get_plus(self):
        return self.__num1 + self.__num2
   
    def get_minus(self):
        return self.__num1 - self.__num2
    
    def get_mul(self):
        return self.__num1 * self.__num2
    
    def get_div(self):
        if self.__num2 == 0:
            return "0으로 나눌 수 없습니다. 다시 입력하세요"
        else:
            return self.__num1 / self.__num2
    
result = Calculate(4,0)
print("더한 값: ", result.get_plus())
print("뺀 값: ", result.get_minus())
print("곱한 값: ", result.get_mul())
print("나눈 값: ", result.get_div())


# 사번 자동 부여
class Employee:
    serial_num = 1000

    def __init__(self, name):
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name

    def __str__(self):  #__str__ : 밑에서 print했을 때 str을 호출한다는 것을 의미(디폴트는 본인타입)
        return (f"사번 : {self.id}, 이름 : {self.name}")
    
e1 = Employee("최사원")
print(e1)
e2 = Employee("안사원")
print(e2)
e3 = Employee("한사원")
print(e3)

employee = [
    Employee('구름'),
    Employee('별'),
    Employee('행성'),
    Employee('달')
]

for i in employee:  #print("\n".join(map(str, employee))) 얘도 가능
    print(i)