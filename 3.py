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