ive = "장원영"
print(ive)
print(f"나는 {ive}입니다.")
print("나는", ive, "입니다.")
print("나는 " + ive + "입니다.")

print(type(77))
print(type(7.2))
print(type("iv\"e"))
print(type('iv\"e'))
a = 77
print(type(a))
a = 7.2
print(type(a))
a = "ive"
print(type(a))
print("111\t111")
print("111\n111")
print("111\"111")
print('111"111')
print("111'111")
print('111\'111')

num = 10
b_num = 0b1010
h_num = 0xA

print(num)
print(b_num)
print(h_num)

print(bin(10))
print(hex(10))

print(ord('0'))
print(ord('A'))
print(chr(48))
print(chr(65))

print(3//2) #몫
print(3.25//2)
print(3%2) #나머지
print(3.25%2)
print(2**3) #n제곱
print(2**10)

print(1+2*3**2)
print(1+(2*(3**2)))
print(1+2*-3**2)
print(1+2*(-3)**2)

print("빵의 개수 :" , 30//4)
print("남은 빵의 개수 :" , 30%4)

a = 1
a += 1 # a = a+1
print(a)

print("장원영" + "럭키비키")
print("럭키"*10)
# print("럭키"*"비키") #에러

song = input("너의 최애 노래는?")
print(song)
print(type(song))

a = input("1+1=?")
print(a)
# print(a+2) a자체가 string(str)이라 에러
print(a*2)
print(int(a)*2)

ff = float(input())

a = 2
print(str(2)*10)
print(str(2)+"입니다")
# print(2+"입니다") #에러

#실습2
print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\__|")

#실습3
name = input("이름을 입력하세요.")
age = input("나이를 입력하세요.")
print("안녕하세요! " + name +"님 "+"("+ age+"세)\n")

name = input("이름을 입력하세요.")
birth = input("태어난 년도를 입력하세요.")
year = input("올해 년도를 입력하세요.")
print("올해는" + year +"년, "+ name + "님의 나이는" + str(int(year)-int(birth)+1) + "세 입니다")



# 리스트
a = []
b = [1,2,3,4]
c = ["장원영", "안유진"]
d = [1, "아이브"]

print(len(c))
print(c[0])
print(c[1])
c[0] = "카리나"
print(c)
del c[0]
print(c)
c. append("asdfe")
print(c)
print(b[-1])
print(b[-2])

# 슬라이싱
seasons = ["봄", "여름", "가을", "겨울"]
print(seasons[0:1])
print(seasons[0:2])
print(seasons[:2])
print(seasons[1:])
print(seasons[2:])
print(seasons[1:3])
print(seasons[::1])
print(seasons[::2])
print(seasons[:])
print(seasons)
print(seasons[::-1]) # 뒤집는거

seasons2 = ["봄", "여름", "가을", "겨울", [1,2,3,4]]
print(seasons2[-1])
print(seasons2[0])
print(seasons2[-1][0])

abcd = "abcd"
abc = ['a','b','c','d']
print(len(abcd))
print(len(abc))

# 실습4 a를 이용해서 짝수, 홀수만 뽑은 리스트 만들기
a =[1,2,3,4,5,6,7,8,9,10]
even = a[1:10:2] # even = a[1::2]
odd = a[0:10:2]
print(even)
print(odd)

# 리스트 함수 - 정렬
a = [3,4,2,1]
a.sort()
print(a)

b = ["a", "c", "d", "b"]
b.sort()
print(b)

c = ["1", "11", "10", "2"]
c.sort()
print(c) # 얘는 정렬안됨 다 str이므로, 얘도 문자라서 사전 순서대로 정렬

d = ["강북", "강남", "서"]
d.sort()
print(d) # 문자는 사전 순서대로 정렬됨(문자랑 숫자는 정렬이 다름)

e = [3,4,2,1]
e.reverse() # = a[::1]
print(e)

e = [3,4,2,1]
e.sort()
e.reverse()
print(e)

# 리스트 함수 - 위치 찾기
f = ["강북", "강남", "서", "asdfe", "서", "서"]
print(f.index("서"))

first = f.index("서")+1 # 두번째에 있는 "서" 위치 찾기
print(first + f[first:].index("서"))

print(f.count("서"))

# 실습1. 다음과 같은 리스트가 있을 때 결과를 출력해보세요.
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
print(rainbow[2]) #1.2번 인덱스 값 출력

rainbow.sort() #2. 알파벳 순서로 정렬한 값 출력
print(rainbow)

rainbow.append("black") #3. 좋아하는 색 맨 마지막에 추가하기
print(rainbow)

del rainbow[3:7] #4. 3~6번째 값 삭제하기
print(rainbow)