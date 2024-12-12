# 파일 입출력 - readlines()
f4 = open("text.txt")
print(f4.readlines())
f4.close


# 파일 입출력 - seek(), tell()
f5 = open("text.txt", "r+")
print(f5.read())
print(f5.tell())
f5.seek(4)
print(f5.write("8"))
f5.close()


# 리스트 랜덤 출력
import random
with open("word.txt", "w") as f:
    word = ["sky", "earth", "moon", "flower", "tree", "apple", "grape", "garlic", "onion", "potato"]
    for i in word:
        f.write(i + "\n")
with open("word.txt", "r") as f:  #단어를 랜덤 추출
    data = f.read().split()  #data = f.readlines() \n인 경우에 이렇게도 가능
    word = random.choice(data)
    print(word)


# 영어 타자 연습 프로그램
import random
import time
import os  #word 파일 찾는 방법

## word = ["sky", "earth", "moon", "flower", "tree", "apple", "grape", "garlic", "onion", "potato"]

if os.path.exists("word.txt"):  #이걸 사용해서 word 파일 찾기. 있으면 그대로 나오고 없으면 에러뜨니까 밑에 파일 추가하면 됨
    with open("word.txt", "r") as f:
        word = f.read().split()  #지역변수 아님

n = 1  #문제번호

input("[타자 게임] 준비되면 엔터!")
start = time.time()

while n < 11:
    print("문제", n)
    question = random.choice(word)
    print(question)
    user = input()
    if question == user:
        print("통과!!")
        n += 1
    else:
        print("오타!! 다시 도전")
end = time.time()
et = end - start
print(f"타자시간 : {et: .2f}초")


# 파일 쓰기 - 입력 받기
with open("./output/input.txt", "a") as f:
    while True:
        text = input("저장할 내용 입력(종료-z)")
        if text == "z" or text == "Z":
            break
            sys.exit(0)
        f.write(text + "\n")


# 실습1. 회원 명부 작성하기
with open("./output/member.txt", "w", encoding="utf-8") as f:  #encoding="utf-8" : 인코딩하는 법(한글로 치면 깨져서 안깨지게 하기 위해)
    for i in range(3):
        name = input("회원의 이름을 입력하시오 : ")
        password = input("회원의 비밀번호를 입력하시오 : ")
        f.write(f"{name} {password}" + "\n")

with open("./output/member.txt", "r", encoding="utf-8") as f:
    print(f.read())


# 실습2. 회원 명부를 이용한 로그인 기능
name = input("이름을 입력하세요 : ")
password = input("비밀번호를 입력하세요 : ")

with open("./output/member.txt", "r", encoding="utf-8") as f:
    for i in f:
        a, b = i.split()
        if a == name and b == password:
            print("로그인 성공")
            break
    else:
        print("로그인 실패")

##for문 안쓰는 방법(dictionary 사용)
dictUser = {}
with open("./output/member.txt", "r", encoding="utf-8") as f:
    for i in f:
        a, b = i.split()
        dictUser[a] = b

name = input("이름을 입력하세요 : ")
password = input("비밀번호를 입력하세요 : ")

if password == dictUser.get(name):
    print("로그인 성공")
else:
    print("로그인 실패")


# 실습3. 로그인 성공 시 전화번호 저장하기
name = input("이름을 입력하세요 : ")
password = input("비밀번호를 입력하세요 : ")

with open("./output/member.txt", "r", encoding="utf-8") as f:
    login_success = False
    for i in f:
        a, b = i.split()
        if a == name and b == password:
            login_success = True
            print("로그인 성공")
            break            
    else:
        print("로그인 실패")
        
if login_success:
    with open("./output/member_tel.txt", "w", encoding="utf-8") as f: 
            phone = input("전화번호를 입력하세요")
            f.write(f"{name} {phone}" + "\n")