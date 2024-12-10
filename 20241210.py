# 실습2. Supermarket 클래스
# class Supermarket:
#     count = 0
#     def __init__(self, location, name, product, customer):
#         self.__location = location
#         self.__name = name
#         self.__product = product
#         self.__customer = customer
#         Supermarket.count += 1

#     def print_location(self):
#         print (f"위치 : {self.__location}")
    
#     def change_category(self, new_product):
#         self.__product = new_product
#         print (f"파는 물건이 {new_product}로 바뀌었습니다.")
    
#     def show_list(self):
#         print (f"현재 파는 물건 : {self.__product}")
    
#     def enter_customer(self):
#         self.__customer += 1
#         print (f"현재 있는 손님 수 : {self.__customer}")
    
#     def show_info(self):
#         print (f"가게 이름 : {self.__name}, 위치 : {self.__location}, 파는 물건 : {self.__product}, 손님 수 : {self.__customer}")
    
#     def show_supermarket_count(self):  #여기에 self빼면
#         print (f"슈퍼마켓 인스턴스 개수 : {Supermarket.count}")
    
# a = Supermarket("포항", "고굽남", "삼겹살", 10)
# b = Supermarket("홍대", "바다회사랑", "회", 15)

# a.print_location()
# a.change_category("된장찌개")
# a.show_list()
# a.enter_customer()
# a.show_info()
# a.show_supermarket_count()  #여기랑


# b.show_info()
# b.show_supermarket_count()  #여기에서 a.b.말고 Supermarket.으로 해야한다


# 클래스 상속
# class Country:  #parent 클래스
#     def __init__(self):
#         self.name = "나라이름"
#         self.population = "인구"
#         self.capital = "수도"

#     def show(self):
#         print("국가 클래스의 메소드")

# class Korea(Country):  #child 클래스
#     def __init__(self, name):
#         self.name = name

#     def show_name(self):
#         print("국가 이름은 :", self.name)

# country = Korea("대한민국")
# country.show()
# print(country.name)
# country.show_name()


# # 메서드 오버라이딩
# class Country:  #parent 클래스
#     def __init__(self):
#         self.name = "나라이름"
#         self.population = "인구"
#         self.capital = "수도"

#     def show(self):
#         print("국가 클래스의 메소드")

# class Korea(Country):  #child 클래스
#     def __init__(self, name):
#         self.name = name

#     def show(self):  #이걸 show로 바꾸면 오버라이딩됨 -> 국가 클래스의 메소드 내용 출력안됨
#         print("국가 이름은 :", self.name)

# country = Korea("대한민국")
# country.show()
# print(country.name)
# # country.show_name()


# 실습3.
# class Calculator():
#     def __init__(self):
#         self.value = 100  #초기 value 값 설정

#     def sub(self, value):
#         self.value -= value  #기본적으로 value 감소시킴

# class MinLimitCalculator(Calculator):
#     def sub(self, value):  #부모 클래스의 sub 메서드 호출
#         self.value -= value
#         if self.value < 0:  #value가 음수가 되지 않도록 설정
#             self.value = 0
#         # self.value = max(0, self.value-value)  #if문 대신 사용가능
#         # super().sub(value)  #if문 대신 이 두줄도 사용 가능
#         # self.value = max(0, self.value)

# cal = MinLimitCalculator()
# cal.sub(20)  #100-20 = 80
# cal.sub(90)  #80-90 = -10 -> 0 출력
# print(cal.value)


# 오버로딩
# class Calculator():
#     def __init__(self):
#         self.value = 100

#     def sub(self, value):
#         self.value -= value

#     # def sub(self):  #메소드 오버로딩(파이썬은 안됨, c언어만 가능)
#     #     self.value -= 10

#     # def sub(self, value1, value2):  #메소드 오버로딩(파이썬은 안됨, c언어만 가능)
#     #     self.value = value1 - value2

#     def sub(self, *args):  #오버로딩하고싶으면 이 방법 사용
#         self.value = args[0]

# a = Calculator()
# a.sub(10)
# print(a.value)


# 모듈 만들기
# import calc_module  #컨트롤누르고 초록색(파일이름) 클릭하면 파일나타남
# print(calc_module.add(1,2))  #파일이름쓰고 점누르면 파일의 기능이 뜬다
# print(calc_module.div(1,2))
# print(calc_module.mul(1,2))
# print(calc_module.sub(1,2))

from calc_module import add
print(add(1,2))