# 과제2. 자판기 프로그램
vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
drink = input("마시고 싶은 음료?")
if drink in vending_machine:     
    print(f"{drink} 드릴게요")
else:
    print(f"{drink}는 지금 없네요") 


# 과제3. 자판기 프로그램 응용
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
print("남은 음료수 : " , vending_machine, "\n")

user = input("사용자 종류를 입력하세요:\n1. 소비자\n2. 주인\n")

if user == "1" or user == "소비자":
    drink = input("마시고 싶은 음료?")
    if drink in vending_machine:
        print(f"{drink} 드릴게요")
        vending_machine.remove(drink)
        print("남은 음료수 : ", vending_machine)
    else:
        print(f"없음")
elif user == "2" or user == "주인":
    action = input("할 일 선택:\n1. 추가\n2. 삭제\n2")
    if action == "1" or action == "추가":
        print("남은 음료수 : ", vending_machine)
        add = input("추가할 음료수?")
        print("추가 완료")
        vending_machine.append(add)
        vending_machine.sort()
        print("남은 음료수 : ", vending_machine)
    else :
        print("남은 음료수 : ", vending_machine)
        delete = input("삭제할 음료수?")
        print("삭제 완료")
        if delete in vending_machine:
            vending_machine.remove(delete)
            print("남은 음료수 : ", vending_machine)
        else:
            print(f"{delete}는 지금 없네요")
else:
    print("잘못된 값입니다. 다시 입력해주세요.")