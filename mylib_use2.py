# mylib 폴더까지 임포트한 경우
from modules.mylib import food

print(food.name)
food.cook()
food.eat()


# food.py까지 임포트한 경우
from modules.mylib.food import name, cook, eat

print(name)
cook()
eat()


# 새로운 파일 임포트하기
import modules2.cm2  #1 : modules2라는 파일 안에 계산기파일(cm2.py)를 만들어서 임포트해봄
print(modules2.cm2.add(1,2))

import calc_module  #기존에 있던 calc_module.py 파일을 임포트함, 결과는 1과 같음
print(calc_module.add(1,2))