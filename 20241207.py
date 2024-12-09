# 연습1. 나누어 떨어지는 숫자 배열
# https://school.programmers.co.kr/learn/courses/30/lessons/12910
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            answer.sort()
    if len(answer) == 0:
        return [-1]
    return answer

## 연습1에 사용할 수 있는 여러 코드들
print(1 if 1>0 else 0)  
print("abc" if 1<0 else "bcd")  #1

if 1<0:  #1과 같음
    print("abc")
else:
    print("bcd")


# 연습2. 두 개 뽑아서 더하기  ##수업 때 배운 set 응용 - 중복이름찾기와 같음
# https://school.programmers.co.kr/learn/courses/30/lessons/68644
## 방법1. 나의 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum not in answer:
                answer.append(sum)
                answer.sort()
    return answer

## 방법2. set이용 -> 이게 시간을 더 절약할 수 있어 not in보다 좋은 코드
def solution(numbers):
    answer = set()
    l = len(numbers)
    for i in range(l-1):
        for j in range(i+1,l):
            answer.add(numbers[i] + numbers[j])
    return sorted(answer)


# 연습3. 하샤드 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12947
## 방법1. 나의 풀이
def solution(x):
    num = sum(list(map(int, str(x))))  #string으로 바꾸는게 중요
    if x % num == 0:
        answer = True
    else:
        answer = False
    return answer

## 방법2. 
def solution(x):
    s = str(x)
    sum = 0
    for i in s:
        sum += int(i)
    return x%sum == 0

# 연습4. 문자열 내림차순으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12917
## 방법1. 나의 풀이
def solution(s):
    l = list(s)
    l.sort()
    l.reverse()
    return ''.join(l)

# ## 방법 2.
def solution(s):
    # answer = ''  
    ls = list(s)
    ls.sort(reverse = True)
    return ''.join(ls)

# ## 방법 3.
def solution(s):
    return ''.join(sorted(s, reverse = True))


# 연습5. 추억점수
# https://school.programmers.co.kr/learn/courses/30/lessons/176963
## 방법1. 나의 풀이 -> 시간이 오래걸림
def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        result = 0
        for j in range(len(name)):
            if name[j] in photo[i]:
                result += yearning[j]
        answer.append(result)
    return answer

## 방법2. dictionary 사용
def solution(name, yearning, photo):
    answer = []
    d = {}
    for i in range(len(name)):
        d[name[i]] = yearning[i]
    for i in photo:
        sum = 0
        for j in i:
            v = d.get(j)
            if v:
                sum += v
        answer.append(sum)
    return answer

## 방법3. dict와 zip 모두 사용
def solution(name, yearning, photo):
    answer = []
    d = dict(zip(name, yearning))
    for i in photo:
        sum = 0
        for j in i:
            v = d.get(j)
            if v:
                sum += v
        answer.append(sum)
    return answer


# 연습6. 크기가 작은 부분문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        l = t[i:len(p)+i]
        if l <= p:
            answer += 1
    return answer


# 연습7. 콜라츠 수열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181919
def solution(n):
    answer = []

    def collat(x):
        answer.append(x)
        if x == 1:
            return
        elif x % 2 == 0:
            collat(x/2)
        else:
            collat(x*3+1)
    collat(n)
    return answer


# 숙련자용1. 특이한 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/120880
def solution(numlist, n):
    answer = []
    d = {}
    for i in numlist:
        d[i] = abs(i-n)
    d1 = sorted(d.items(), key = lambda item:(item[1], -item[0]))
    print(d.items())
    print(d1)
    for i in d1:
        answer.append(i[0])
    return answer


# 숙련자용2. 옹알이(1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120956
def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in can:
            idx = i.find(j)
            if idx > -1:
                print(idx, i, j)
                i = i.replace(j, '_')
                print(idx, i, j)
        i = i.replace('_', '')
        if len(i) == 0:
            answer += 1
    return answer


# 숙련자용3. 하노이의 탑
# https://school.programmers.co.kr/learn/courses/30/lessons/12946
def solution(n):
    answer = []
    def hanoi(n, f, t, v):
        if n == 1:
            answer.append([f,t])
        else:
            hanoi(n-1, f , v, t)
            answer.append([f,t])
            hanoi(n-1, v, t, f)
    hanoi(n, 1 , 3, 2)
    return answer