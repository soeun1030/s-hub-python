# 튜플
t1 = (10, 20, 30)
print(type(t1))
print(t1)
print(t1[0])  #t1[0] = 3 안됨
del t1  #del t1[0]은 안됨

t2 = (10)
t3 = (10,)
t4 = 10,
print(type(t4))


# set
set1 = {1, 2, 3}
print(set1)
set2 = set([1,2,3,3])
print(set2)
set2.add(4)
print(set2)
while len(set2) > 0:
    a = set2.pop()
    print(a)

l1 = [1,2,3,4]
while len(l1) > 0:
    a = l1.pop()
    print(a)

set3 = set("apple")
print(set3)
while len(set3) > 0:
    a = set3.pop()
    print (a)


# set 응용
name = ["1", "2", "3", "2"]

for i in range(len(name)):
    if name.count(name[1]) > 0:
        print(name[i])

name_set = set(name)
print(name_set)
name_list = list(name_set)
name_list.sort()
print(name_list)

# for루프 이용해서 중복 제거하기
name = ["1","2","3","2"]
a = []
for i in range(len(name)):
    if a.count(name[i]) < 1:
        a.append(name[i])
name = a
print(a)


# 딕셔너리
a = {}
print(type(a))
b = {1}  #set()
print(type(b))
c = dict()
c = {1:'a', 'b':'b'}
print(c)
c[2] = 'c'  #인덱스가 아니라 key
c['c'] = 2
print(c)
del c[2]
del c['b']
print(c)
print(c.get(2))
print(c.keys())
print(c.values())

for i in c.keys():
    print(i, c.get(i))

print('c' in c)  #print('c' in c.keys())와 같음
print(2 in c.values())


# 딕셔너리 응용 - try랑 except KeyError 안쓰고 작성하기
## 방법1
dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}


print("★ 컴퓨터 사전 ★")
word = input("검색할 단어를 입력하세요: ")

if word in dic:
    print(f'{word}: {dic[word]}')
else:
    print("정의된 단어가 없습니다.")

## 방법2
dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}


print("★ 컴퓨터 사전 ★")
word = input("검색할 단어를 입력하세요: ")
value = dic.get(word)
if value:
    print(f'{word}: {dic[word]}')
else:
    print("정의된 단어가 없습니다.")


# 실습1. set 사용
n, m = map(int, input().split())  # n과 m 입력
s = set()  #집합 s 초기화

for i in range(n):  #집합 s 구성
    s.add(input())  #s에 문자열 추가

count = 0  #교집합 개수 카운트
for i in range(m):
    word = input()
    if word in s:  # word가 s에 있으면
        count += 1
print(count)


# 실습1. list, dic 사용
n, m = map(int, input().split())  # n과 m 입력
dic = {}  #문자열을 저장한 dictionary 생성

for _ in range(n):  #첫번째 집합 s 구성
    word = input()
    dic[word] = True  #key로 문자열 저장, value는 True

count = 0  #교집합 개수 카운트
for _ in range(m):
    word = input()
    if word in dic:  #dictionary에 word가 있으면
        count += 1
print(count)


# 실습2. 딕셔너리 사용
students = {"Alice" : 85, "Bob" : 90, "Charlie" : 95}
students["David"] = 80
students["Alice"] = 88
del(students["Bob"])
for i in students.keys():  #.keys 디폴트이므로 굳이 안써도됨
    print(i, students.get(i))


# 2차원 리스트
d = [
    [10, 20],
    [30, 40],
    [50 , 60]
]

print(d)
print(d[0][0])
print(d[1][1])
d.append([70,80])
print(d)
d[0][0] = 90
print(d)

del(d[1][1])  #d[1].pop(1)
print(d)  #print(d[1][1]) 위에서 d[1][1] 지웠으므로 이거 출력하면 에러
print(len(d))
print(len(d[0]))

for i in range(0,len(d)):
    for j in range(0,len(d[i])):
        print(d[i][j], end=" ")
    print()

for x, y in d:  #위에 del(d[1][1])지워야 출력됨
    print(x,y)