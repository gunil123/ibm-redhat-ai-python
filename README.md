# IBM x RED HAT AI과정
## python

## 02-27 수업내용
```python
#Q1 계산기 함수 만들기
def calc(oper, *args):
    if oper == "add":
        return sum(args)

    elif oper == "mul":
        multi = 1
        for i in args:
            multi *= i
        return multi
    elif oper == "avg":
        return sum(args)/len(args)
    else:
        raise ValueError('잘못된 연산이다')
print(calc("add", 1,2,3)) #6
print(calc("mul", 1,2,3,4)) # 24
print(calc("avg", 10,20,30)) # 20
```
---

```python
#Q2. 나이 입력 프로그램
#사용자 정의 예외(예외를 만듬)
class AgeError(Exception):
    pass
try:
    age=int(input('나이 입력'))
    if(age<=0):
        raise AgeError('나이는 0이상이어야해')
  
    print('입력 완료')
except ValueError:
    print('숫자 입력해야돼!')
```

---
```python
#Q3. 회원 관리
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.id}, {self.name}, {self.email}"
    
class UserManager:
    def __init__(self):
        self.user = []
    def add_user(self, user):
        self.user.append(user)

    def delete_user(self, user_id):
        self.user = [i for i in self.user if i.id!=user_id]    
    
    def li_user(self):
        for i in self.user:
            print(i)
    
    def find_user(self, user_id):
        for i in self.user:
            if i.id == user_id:
                return i
        return None

user1 = User(1, "홍길동", "hong@aa.com")
user2 = User(2, "김길동", "kim@aa.com")
user3 = User(3, "박길동", "park@aa.com")

manager = UserManager()
manager.add_user(user1)
manager.add_user(user2)
manager.add_user(user3)

find_id = 2
result = manager.find_user(find_id)

if result:
    print(f"조회된 유저: {result}") # print 뒤에 내용을 채워넣었습니다.
else:
    print(f"ID {find_id}번 유저를 찾을 수 없습니다.")
# 전체 목록 조회 및 삭제 테스트
manager.li_user()
print("=================")
manager.delete_user(1)
manager.li_user()
```
---
```python
#Q4.
#무한대로 짝수를 생성해라
def even_gen():
    n = 0
    while True:
        yield n
        n += 2

g = even_gen()
print(next(g))
print(next(g))
print(next(g))
```

```python
#Q5.
# 파일 처리

def score1(name, score):
    try:
        with open('score1.txt', 'a', encoding='utf-8') as f:
            f.write(f"{name},{score}\n")      
        print(f"{name}님의 데이터가 메모장에 읽기 좋게 저장되었습니다.")
    except ValueError:
        print("점수는 숫자로 입력하세요")

def average():
    sum=0
    cnt=0
    try:
        with open('score1.txt', 'r', encoding='utf-8') as f:
            for i in f:
                i=i.strip()
                name,score=i.split(",")
                sum+=int(score)
                cnt+=1
        return sum/cnt       

            
    except FileNotFoundError: 
        print("파일이 없습니다.")
        return None

# 실행
score1('홍길동', 100)
score1('김길동', 150)

avg=average()
print(avg)
```
---
```python
#Q6.
login_state=False

def login(func):
    def wrapper(*args, **kwargs):
        if not login_state:
            print('로그인')
            return
        return func(*args, **kwargs)
    return wrapper
@login #데코레이터함수
def write_post():
    print("글 작성 완료")
write_post()   #로그인
login_state = True
write_post() #로그인

#write_post 함수에 @login 데코레이터 적용시킴 -> wrapper()실행됨
```
---
## json
- json은 JSON 데이터를 쉽게 처리하고자 사용하는 모듈이다.
- JSON 파일을 읽을 때는 json.load(파일_객체)를 사용한다.
- JSON 파일로 생성할 때는 json.dump(딕셔너리, 파일_객체)를 사용한다.
```json
[
{
    "name" : "tom",
    "score" : 100
},
{
    "name" : "Juli",
    "score" : 80
}
]
```
---
```python
import json

def loading():
    try:
        with open('stu.json', 'r', encoding='utf-8')as f:
            return json.load(f)
        
    except FileExistsError:
        print("파일없음")

def add(data):
    with open('stu.json','w', encoding='utf-8')as f:
        json.dump(data,f, ensure_ascii=False, indent=2) #ensure_ascii=False - 아스키 문자열로 변경되는 것을 방지,
                                                        # indent - 문자열을 정렬한다.
#print(loading())
datas=[{"name" : "tom", "score" : 100},
{"name" : "Juli","score" : 80}
]
add(datas)
print('저장')
```


---

## 02-26 수업내용

### 내장함수
```python
#chr : 아스키 -> 문자, ord: 문자 -> 아스키
print(chr(65))
print(ord('A'))

#enumerate : 인덱스 + iterable 객체
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# filter : 반복가능한 객체 요소를 지정한 후 조건에 맞는 값 추출
def num(x):
    return abs(x) > 3
print(list(filter(num, [-3,2,4,-4,-10,-100])))

# lambda로 바꾸기
print(list(filter(lambda x : abs(x)>3, [-3, 2, 4, -4, -10, -100])))

# id : 객체의 주소값 반환
print(id(int(10)))
print(id(10))
print(id(11))

#len : 길이반환
print(len('python'))
print(len([1,2,3,4,5]))

#p.250
#map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
# 반복가능한 객체 : 리스트, 튜플, 문자열

def num2(x):
    return x
#map(함수명넣어서)
#map(lambda)
print(list(map(num2, [1,2,3,4,5])))

print(list(map(lambda x:x, [1,2,3,4,5,6])))

#range: 반복가능한 객체 반환
print(range(5))
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,10,-1)))

for i in range(5):
    print(i)

#p. 251
# max, min 최대, 최소
print(max([100,223,34242]))
print(min(1,2,3))

#round : 반올림
print(round(4,6))
print(round(3.12421414,2))

#sorted: 반복가능한 객체 정렬 후 반환
print(sorted([5,6,2,1,3,4,3,3,4]))
a = sorted([4,5,6,2,1,2,4,2])
print(a)
print(sorted(['p', 'y', 'y', 'h', 'o', 'n']))

#sum : 반복가능한 객체 합 반환
print(sum([1,2,3,45]))

#type : 자료형 확인
print(type(3))
print(type({}))
print(type(()))
print(type([]))

#p.225
#zip: 반복가능한 객체의 요소 묶어서 반환(인덱스 순서대로 묶임)
print(list(zip([10,20,30], [40,50,60])))
```




---

## 02-25 수업내용


---
## 02-24 수업내용

## 함수
- 파이썬의 함수 구조
```python
def 함수_이름(매개변수):
    수행할_문장1
    수행할 문장2
```
### 매개변수(parameter)와 인수(arguments)
- 매개변수는 함수에 입력으로 전달된 값을 받는 변수
- 인수는 함수를 호출할 때 전달되는 입력값을 의미
```python
def add(a,b): #a,b는 매개변수
    return a + b
print(add(3,4)) #3,4는 인수
```
### 일반적인 함수
- 리턴값이 있는 함수
```python
def func1(x):
    y1 = x * 5
    y2 = x * 10
    y3 = x * 20
    return(y1,y2,y3)
a=func1(5) #a의 값은 return 값
print(a, type(a))   # (25, 50, 100) <class 'tuple'>
```
### 매개변수 지정하여 호출하기
```python
def sub(a,b):
    return a - b
result = sub(a=7, b=3)
print(result)
```
---
## 여러 개의 입력값을 받는 함수 만들기
- **(*args)** 을 사용하여 입력값을 여러 개를 받는다.
```python
def func1(*args):
    for i in args:
        print(i)
func1('gildong')
func1('gildong', 'tom', 'juli')
func1('gildong', 'tom', 'juli','jack')
```

### 키워드 매개변수, kwargs
- 키워드 매개변수를 사용할 때는 매개변수 앞에 별 2개를 붙인다.
```python
## *kwargs
def func2(**kwargs):
    for i in kwargs.keys():
        print(i, kwargs[i], type(i), kwargs, type(kwargs))
func2(name1 = '철수')
func2(name1 = '영수', name2='영희', name3='철희')
func2(name1 = '바보', name2='영미')

def func3(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)
func3(10,40,'kim','lee''park',age=10, ader='seoul')
```
### 함수의 리턴값은 언제나 하나이다.

---
### 초기값 설정
- 매개변수에 초기값을 미리 설정
```python
def say(name, man, old=20):
    print(name)
    if man:
        print('남자', old)
    else:
        print("여자", old)
say('jili', True)
say('tom', False, 10)
```
### 함수 안에서 선언한 변수의 효력 범위
```python
a = 1   # 함수 밖의 변수 a
def vartest(a):  # vartest 함수 선언
    a = a + 1
    return a
    
a = vartest(a)    #vartest 함수의 입력값으로 a를 대입
print(a)    # a값 출력 (1출력됨)
```
- 함수 안에서 사용하는 매개변수는 함수 안에서만 사용하는 '함수만의 변수' 이다.
- 매개변수 a는 함수 안에서만 사용하는 변수일 뿐, 함수 밖의 변수 a와는 전혀 상관없다

### 함수 안에서 함수 밖의 변수를 변경
1. return 사용하기
2. global 명령어 사용하기
---

### lambda 예약어
- 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을하고, 줄 간결하게 만들 때 사용
```python
# 함수명 = lambda 매개변수:실행문
add = lambda a, b: a + b
result = add(3,4)
print(result)
#람다 왜쓰냐
#가독성 좋음, 코드간결,메모리 절약
#즉시 실행 함수 -> 정의하자마자 바로 실행됨

multi = lambda x, y : x * y
print(multi(3, 4))

a = multi #함수명을 a에 할당함(a는 alias - 별칭이 됨)
print(a(4, 5))
```
---

## 사용자의 입출력
### input 사용하기
```python
name = input('이름은?')
score = input('학점은?')
age = input('나이는?')
print(name,score,age)
print(type(name), type(score), type(age))

num1 = int(input('첫번째 정수')) #문자열 타입 -> 숫자(정수)타입으로 변경
num2 = int(input('두번째 정수'))
print(num1 + num2)
```

### print 자세히 알기
- 큰따옴표로 둘러싸인 문자열은 +연산과 동일하다
- 문자열 띄어쓰기는 ,쉼표로한다. (**문자열 띄어쓰기 가능**)
---

## 파일 읽고 쓰기
### 파일 생성하기
```python
# 파일 입출력
# 읽기: r, 쓰기, w(파일생성), 추가 : a
#파일 읽기
# 절대 경로(C:/test/news.txt), 상대경로("../, ./")
#인코딩 : 문자를 숫자로 바꾸는 것
#디코딩 : 숫자를 문자로 바꾸는 것
#UTF-8 : 가장 많이 쓰는 국제 표준 인코딩(유니코드)
#encoding = 'UTF-5'

f = open("새파일.txt",'w')
f.close() # 파일 객체를 닫아주는 역할 한다.
```
### 파일을 쓰기 모드로 열어 내용 쓰기
```python
with open('./resource/test.txt', 'w') as f: #test1.tsx 파일 생성하여 읽음
    f.write('h1 python!!\n') #test1.tsx 파일에 문자열 쓰기
```   
---

### readline 함수 이용하기
```python
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
    line=f.readline() #한 줄씩 출력
    print(line)
    line = f.readline()
    print(line)
```
### readlines 함수 이용하기
```python 
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
    lines=f.readlines() #한 줄씩 출력
    print(lines)
    for i in lines:
        print(i)
```
### read 함수 사용하기
```
result = f.read()
print(result)
f.close()
```
---

### 파일객체를 for문과 사용 - 파일을 줄 단위로 읽을 수 있다.
```python
f = open('./resource/news.txt', 'r', encoding='UTF-8')
for line in f:
    print(line)
f.close()
```
### 파일에 새로운 내용 추가하기
```python
with open('./resource/test.txt', 'a') as f: # 문자열 append
    f.write('h1 react!!\n')  

# 줄바꿈을 자동으로 추가안함 : writelines         
with open('./resource/test.txt', 'a') as f:
    li=['React\n','DB\n','Python\n']
    f.writelines(li)
```
### with을 사용하여 파일을 열면 항상 닫아주게 한다.
### CSV(Comma Seperated Values) - csv 파일 불러옴
---

## 클래스
- 과자 틀 = 클래스, 과자 틀로 찍어 낸 과자 = 객체, 클래스 안에 구현된 함수 = **메서드**
---
### 객체와 인스턴스의 차이
- 인스턴스 -> 클래스로 만든 객체
```python
class Cookie:
    pass
a = Cookie() # a객체는 Cookie의 인스턴스이다.
b = Cookie()
```
```python
# class 설계도
# object 설계도를 바탕으로 실제 만들어진 제품

# 클래스
# self, 인스턴스 메소드, 인스턴스 변수
# 클래스 메소드, 클래스 변수

#객체(object) : 클래스의 인스턴스를 포함한 모든 파이썬 데이터 //123,"Hello",[1,2,3]
#**인스턴스(instance) : 특정 클래스에 의해 생성된 객체를 지칭할 때
from copy import copy
class Profile:
    names="gildong" #클래스 변수(클래스 블록 안 - 모든 인스턴스 접근가능(공유))

    #초기화 함수(self:객체 자기자신)
    def __init__(self, name, age): #인스턴스 변수 : 각 인스턴스마다 개별적으로 존재
        self.name=name  #self를 안적으면 지역변수임 => 인스턴스에 저장되질 않음
        self.age = age

p = Profile("gilding", 13)  #Profile클래스의 인스턴스, 객체가 생성되면 __init__함수 자동 호출됨
p2 = Profile("jiji", 23)
```
- 인스턴스 메서드()를 클래스 이름으로 직접 호출할 때는, 생략되던 self 자리에 인스턴스 객체()를 명시적으로 전달해야 한다.
```python
class Test:
    # def func1():
    #     print("Func1!!") #self 인자가 없는 일반 함수 --> 클래스 안에 있지만 인스턴스 메소드 아님

    def func2(self):   #인스턴스 메소드로 호출 시 자동으로 self(인스턴스 객체 자신)가 전달됨
        print(id(self)) 
        print("Func2!!")
t = Test()
# t.func1() #에러 -> func1()에 self가 없는데, t.func()호출 시 파이썬 내부적으로 func1(t)호출하려 한다.
t.func2()

# Test.func1() #클래스에서 직접호출
#Test.func2() #예외 -> func2(self)인데 인자 없이 호출해서 self(Test의 인스턴스)가 없어 예외
Test.func2(t) # 직접 인스턴스 t를 self로 넘겨 호출
```


---
## 02-23 수업내용

## 집합 자료형 - set
- 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형
```python
# 순서(x), 중복(x)
s1 = set()
s2 = set([1,2,3,4]) #리스트 자료형을 집합 자료형으로 변환

s3 = set([1,4,6,7])
s4 = set([1,2,'apple','mango','python'])
s5 = {'phone', 'computer','notebook', 'water','phone'}
s6 = {12, 'mouse', (1,2,3),3.14}

print(type(s1),type(s2),type(s3),type(s4))
#s2를 튜플로 변환
t = tuple(s2)
print(t, type(t))
# 튜플로 변경했기 때문에 인덱스 사용가능
print(t[0], t[1:3])

# s3,s4 list 변경
# 리스트로변경했기 때문에 인덱스 사용가능
li = list(s3)
li2 = list(s4)
print(li[0], li2[1:3])
```
### 교집합, 합집합, 차집합 구하기
```python
et1 = set([1,2,3,4,5,6])
set2 = set([4,5,6,7,8,9])

print(set1&set2)   #교집합 456
print(set1.intersection(set2))  #교집합

print(set1|set2) #요소 중복 제거되면서 합쳐짐
print(set1.union(set2))  #합집합

print(set1-set2) #{} set1에는 있지만 set2에 없는 요소들
print(set1.difference(set2)) #차집합
```

### 집합 자료형 관련 함수
- 값 1개 추가하기 - **add**
- 값 여러 개 추가하기 - **update**
- 특정 값 제거하기 - **remove**
- 다 제거 -**clear**(요소만 사라짐, 구조 남아있음)
---
## 불 자료형
- 참과 거짓을 나타내는 자료형이다. True, False 값을 가진다.
```python
a = True
b = False
print(type(a)) #<class 'bool'>
print(type(b)) #<class 'bool'>
```
- 0: 거짓, None : 거짓

### 리스트를 복사하고자 할 때 
```python
a = [1,2,3]
b = a
print(a is b)  # True / a와 b는 완전히 동일
```
### copy 모듈 이용하기 p.114
```python
#from 모둘명 import 함수
from copy import copy
a2=[1,2,3] #복사를 했지만 요소만 복사/ 주소값은 복사하지않음
b2 = copy((a2))  
print(b is a)  #False b와 a가 가리키는 객체는 서로 다르다
```
---
## if문
- if문에 속하는 모든 문장 들여쓰기 한다.
```python
if True:
    print('참')
else:
    print('거짓')
x = 20
y = 10
print(x==y)
print(x!=y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
```
--- 
## and, or, not
- 조건을 판단하기 위해 사용하는 연산자로 and, or, not 이 있다.
```python
print(a>b and b>c)
print(a>b or b>c)
print(not a>b)
print(not b>c)
print(not True)
print(not False)
```

## in, not in
- x in 리스트, x not in 리스트
- x in 튜플, x not in  튜플
- x in 문자열, x not in 문자열

```python
x = [10,20,30] #list
y = {70, 80, 90, 100} #set
z={"name":"kim", "city":"seoul", "id":"gildong"} #dict
m=(10, 20, 24) #tuple

print(25 in x)
print(90 in y)
print(20 not in m)

print("city" in z)
print("gildong" in z.values()) #값들에 gildong값이 있는지 확인
```
---
## 다양한 조건을 판단하는 elif
```python
score = 90
if score>=90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
```
---
## 조건부 표현식
- 파이썬의 조건부 표현식을 사용하면 코드를 간단히  표현할 수 있다.
```python
message = "succes" if score>=60 else "failuer"
```

---
## while문 만들기
```python
#초기 조건 증감
#while 조건:
# 반복할 실행코드

num =5 
while num>0:
    print(num)
    num=num-1

a = ['a', 'b', 'c']

while a: #리스트에 값이 있으므로 True로 인식
    print(a.pop())  #마지막 값 반환
```
- break는 반복문을 탈출하고, continue는 처음으로 돌아가서 반복문 다시 실행한다.
- While True: 를 사용하면 무한 루프를 사용할 수 있다.
---

## for 문
```python
test_list=['one','two','three']
for i in test_list:
    print(i)
# for i in collecton:
# 반복할 실행코드

names=['kim','lee','park','choi']
for i in names:
    print(i)

profile={
"name":"hong",
"age" : 33
}

for i in profile:
    print(i) #키값을 반환한다.
    print(profile[i]) #Value 값 반환한다.

#is: 두 객체가 같은 객체(메모리 주소가 같은지) 인지 비교하는 연산자!
li=["3",1,2,True,4.5]
for i in li:
    if type(i) is str:
        continue
    print(i, type(i))
```
### for문과 함께 자주 사용하는 range 함수
- range(1,11)은 숫자 1부터 10까지의 숫자를 데이터로 가지는 객체이다.
```python
add = 0
for i in range(1,11):
      add = add + i
print(add) # 55
```
### 리스트 컴프리헨션 사용하기
- 리스트 안에 for문을 포함하는 리스트 컴프리헨션을 사용하면 좀 더 편리하고 직관적으로 만들 수 있다.
```python
# 구구단 리스트 컴프리헨션 사용하여 구현
result = [x*y for x in range(2,10)
      for y in range(1,10)]
print(result)
```
## 함수
```python
#함수
#개발자가 함수명 통해서 정의한 후에 필요할 때마다 호출
#반복되는 코드를 한번 구현 한후 재사용 가능하도록 만든 코드의 집합
#함수 구현 후 -> 재사용

#매개변수가 있는 함수
#매개변수가 업는 함수
#결과값 반환하는 함수(return)
#결과값 반환 안하는 함수

def func1(): #매개변수가 없는 함수
    print("함수1")
#함수 호출 -> 함수실행
func1()

def func2(a,b): #매개변수가 있는 함수
    print(a,b) #결과값 반환 안하는 함수

func2(1,2)

def func3(a,b): #매개변수가 있는 함수
    return(a+b)  #결과값 반환하는 함수(return)

print(func3(10,20))
```

---

## 02-20 수업내용

### 자리 확보
```python
print('%3d' %(12321313221313123))  #12321313221313123
# 최소 3자리 공간을 확보해서 출력해줘
#최대 길이를 제한하는것이 아님
```

### f문자열 포메팅
- 문자열 앞에 f 접두사를 붙이면 f문자열 포매팅 기능 사용할 수 있다.
```python
name = '홍길동'
age=30
str1=f'내 이름은 {name}입니다. 나이는 {age}입니다'
print(str1)
```
### f문자열 포메팅 - 정렬
```python
print(f"{'hello':>10}")

n=50
print(f"{n:<20}")
print(f"{n:>10}")
```

---
### 문자 개수 세기-count
- count 함수로 문자 개수 리턴
```python
a = "hobby"
print(a.count('b')) #2
```
### 위치 알려주기 1-find
- 문자열 중 문자가 처음 나온 위치 반환하고, 존재하지 않으면 -1
```python
a = "Python is the best choice"
print(a.find('b')) #14
print(a.find('k')) #-1
```
### 위치 알려주기 2-index
- 문자열 중 문자가 처음 나온 위치 반환하고, 존재하지 않으면 **오류 발생**
```python
a = "Python is the best choice"
print(a.index('b')) #14
```
---

### 문자열 삽입 -join
```python
result = ",".join('abcd')
print(result)  #a,b,c,d

letters = ['a', 'b', 'c', 'd'] #리스트나 튜플도 입력으로 사용 가능
```

### 소문자를 대문자로 바꾸기 -upper, 대문자를 소문자로 바꾸기 - lower
```python
a = "hi"
print(a.upper())  #HI
a = "HI"
print(a.lower())  #hi
```
---

### 왼쪽 공백 지우기 - lstrip, 오른쪽 공백 지우기 - rstrip, 양쪽 공백 지우기 - strip
```python
a = " hi "
print(a.lstrip())  #hi
print(a.rstrip())  # hi
print(a.rstrip())  #hi
```
### 문자열 바꾸기 - replace, 문자열 나누기 - split
```python
a = "Life is too short"
print(a.replace("Life", "Your leg")) #Your leg is too short
print(a.split())  #['Life', 'is', 'too', 'short']
```

- upper, lower, join, rstrip, lstrip, strip, split 등 함수는 문자열 자체의 값이 변경되는 것 이 아니라 **변경된 값을 리턴**한다는 사실에 주의!!
 ```python
a = 'hi'
print(a.upper()) #HI
print(a) #hi
```
---

### 리스트 자료형(순서 o, 중복 o, 수정 o, 삭제 o )
- 파이썬에서는 배열 제공하지 않는다
```python
list3 = [60, 100, 98, 95]
a = []
```
### 리스트 인덱싱과 슬라이싱
- 리스트도 문자열처럼 인덱싱 적용 가능
```python
a = [1,2,3]
print(a) #[1,2,3]
print(a[0])  #1
print(a[0] + a[2]) #4
print(a[-1])  #3  a[-1]은 문자열과 마찬가지로 리스트 a마지막 요솟값 말함
```

- 리스트도 문자열처럼 슬라이싱 기법 적용 가능
```python
a = [1,2,3,4,5] 
print(a[0:2]) #[1,2]
```
- 문자열 값만 추출하고 싶을 때
```python
list4=[1000,1000,'Tom','Juli',"Jack"]

# list4 문자열만 추출
list4_strings = [x for x in list4 if isinstance(x, str)]
# isinstance(값, 자료형)-(true/false반환) 함수는 변수가 특정 자료형인지 확인하는 함수
print(list4_strings)
```

---
### 리스트 연산하기
- +를 사용해서 더할 수도 있고 *를 사용해서 반복할 수 있다.
```python
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)   #[1, 2, 3, 4, 5, 6]
```
### 리스트 길이 구하기 - len 함수
```python
a = [1, 2, 3]
print(len(a)) # 3
```
### 리스트 연산 오류
```python
a = [1, 2, 3]
print(a[2] + "hi") # 오류! 
print(str(a[2] + "hi"))  #a[2]의 값을 문자열로 변경
```

---

### 리스트의 수정과 삭제
- 리스트의 값을 수정하거나 삭제할 수 있다.
```python
a = [1, 2, 3]
a[2] = 4
print(a)  # [1, 2, 4]

del a[1]
print(a)  # [1, 4]
```
- del a[ x]는 x 번째 요솟값을 삭제한다.
- 슬라이싱 기법 통해 del a[ 2:] 리스트 요소 여러 개를 한꺼번에 삭제할 수 있다.
---
### 리스트 관련 함수
- 리스트에 요소 추가하기 - **append**
- 리스트 정렬 - **sort**
      - 리스트의 요소를 순서대로 정렬
- 리스트 뒤집기 - **reverse**
      - 리스트를 역순으로 정렬하는 것이 아닌 리스트를 그대로 거꾸로 뒤집는다
- 인덱스 반환 - **index**
- 리스트에 요소 삽입 - insert
      - insert(a,b)는 리스트의 a번째 위치에 b를 삽입하는 함수
```python
a = [1, 2, 3]
a. insert(0, 4)
print(a)  # [4, 1, 2, 3]      
```
- 리스트 요소 제거 - remove
- 리스트 요소 끄집어 내기 - pop
      - pop()은 리스트의 맨 마지막 요소를 리턴하고 그 요소는 삭제한다.
- 리스트를 바꾸는 함수들은 대부분 반환값이 None임
- 리스트에 포함된 요소 x의 개수 세기 -count
      - count(x)는 리스트 안에 x가 몇 개 있는지 조사하여 그 개수 리턴하는 함수
- 리스트 확장 - extend
      - a.extend([ 4,5])는 a+=[4,5 ]와 동일하다.

- 슬라이싱에서 간격줘서 일부분 자르기
```python
a="abcdefg"
print(a[0:5:2]) #ace

#리스트명[초기인덱스 : 끝인덱스 : 증감]
```

---

### 튜플 자료형
- 튜플은 ()로 둘러싼다.
- 리스트는 요솟값의 생성, 삭제, 수정이 가능하지만, 튜플은 ( 전체)삭제만 가능하고 요솟값을 바꿀 수 없다.
- 요소 뒤에 ,쉼표를 반드시 붙여야하고, ()소괄호 생략 가능하다.

### 튜플 - 인덱싱하기
- 문자열, 리스트와 마찬가지로 인덱싱 가능하다.
```python
t1 = (1, 2, 'a')
print(t1[0])  # 1
```
- 튜플은 요솟값이 바뀌지는 않지만, 인덱싱, 슬라이싱, 더하기, 곱하기, 길이 구하기는 가능하다.

---

### 팩킹과 언팩킹
- 팩킹(packing) : 여러 값을 하나의 튜플, 딕셔너리, 리스트 등으로 묶는 것
- 언팩킹(unpacking) : 튜플, 딕셔너리, 리스트 등으로 묶여 있는 값을 개별(각각) 변수로 푸는 것
```
x = 2
y = 3
z = 4
pack1 = (x, y, z) #packing
pack2 = [x, y, z] #packing
print(pack1)   #(2, 3, 4)

(x,y,z) = pack1 #unpacking
print(x, y, z) #2 3 4
```
### 튜플 더하기 
```python 
a = (1, 2, 3)
a = a + (4,)  #(4,) 라는 튜플을 더한다. a값이 변경되는 것 아니라 새로운 튜플이 생성되고, 그 값이 변수에 대입. a고유 주소 값 변경됨
print(a) 
```

### 딕셔너리
- 순서x, 키 중복 x, 수정 O, 삭제 O
- '사전'이라는 뜻으로, 리스트나 튜플처럼 순차적으로 
해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다.

- {}중괄호 사용하고, dict() 함수를 이용할 수 있다.
- dict()는 키가 문자열이고, 변수 규칙을 따를 때만 가능, (키, 값) 형태의 튜플이 모이면 가능
```python
dic1 = {'name':'Lee', 'phone':'010-1234-1234', 'borth':'00021'} #그대로 dict 출력

dic6=dict([('name','tom'), ('addr','seoul'), ('age' , '22'), ('grade','A'),('status',True)])
# {'name': 'tom', 'addr': 'seoul', 'age': '22', 'grade': 'A', 'status': True}  
# 가장 안쪽 구조 : 튜플 구조
# 안쪽을 감싸는 구조 : 리스트 구조(여러 개의 튜플을 하나로 묶음 -> 튜플의 리스트)
# 가장 바깥쪽 구조 : 딕셔너리 구조로 변환해줘

#(키, 값 )튜플 -> 튜플들의 리스트 -> dict() - > 딕셔너리{키:값} 
```
### 딕셔너리 쌍 추가, 삭제하기
```python
dic1['address']='yougsan' # 쌍추가

del a[1] # key가 1인 Key:Value 쌍삭제
print(a)

print(dic1.pop('name')) #키 값 넣어서  삭제 -> 값도 같이 삭제됨
print(dic1)  # pop으로도 삭제 가능
```
### 딕셔너리에서 Key 사용해 Value 얻기
```python
grade = {'pey':10} # Key가 'pey'인 딕셔너리 Value를 반환
print(grade['pey']) #10   
```
### 딕셔너리 만들 때 주의사항
- 딕셔너리에는 Key는 고유한 값이므로 중복되는 Key값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다.
```python
# 기존 값 덮어씀(키값 중복되면)
a={1:'c', 1: 'a', 1:'b', 1: 'd'}
print(a)
```
- 또, 키에 리스트는 []쓸 수 없다. (오류 발생)

---
### 딕셔너리 관련 함수 

#### Key 리스크 만들기 -Keys()
```python
print(dic1.keys()) #키들의 집합
print(dic2.keys())  # dict_keys(['name', 'phone', 'borth', 'address'])

print(list(dic1.keys())) #리스트형으로 변환해서 출력 
# ['name', 'phone', 'borth', 'address']
```
#### Value 리스트 만들기 values()
```python
print(dic1.values()) #값(value)들의 집합
# dict_values(['Lee', '010-1234-1234', '00021', 'yougsan'])
print(list(dic1.values())) #리스트형으로 변환해서 출력
# ['Lee', '010-1234-1234', '00021', 'yougsan']
```
#### Key, Value 쌍 얻기 - Items()
```python
print(dic3.items()) #키, 값 쌍 다 출력
# dict_items([('ary', [1, 2, 3, 4])])
print(list(dic3.items()))  #리스트형 변환해서 출력
#[('ary', [1, 2, 3, 4])]
```
#### Key, Value 쌍 모두 지우기 - clear()
```python
a.clear()
print(a)   # {}
```
#### Key로 Value 얻기 - get()
- get(x)함수는 x라는 Key에 대응되는 Value를 리턴한다. 존재하지 않는 값을 가져오려하면 None을 리턴한다.
```python
print(dic1.get('name'))  #Lee
print(dic1.get('name1'))  #None

print(dic1['name1'])
# print(dic1['name1']) #키 값이 있으면 출력, 없으면 **keyError*

# 키가 없는 경우 기본값도 줄 수 있다.
print(dic1.get('name1', 0))  # 0
```
#### 해당 Key가 딕셔너리 안에 있는지 조사하기 -in
- 해당 Key를 찾아 있으면 True, 없으면 False
```python
print('name' in dic1)
# True
print('name1' in dic1)
# Flase
```

---

## 02-19 수업내용

### python 파일 설치 3.11버전, 파이썬에서 주석은 (#

### 숫자형(정수, 실수 8진수, 16진수)
```python
a = 123
a = -178
a = 0
```

### 파이썬 자료형
```
int 정수
float 실수
complex 복소수
bool 불린
str 문자열
list 리스트
tuple 튜플
set 집합
dict 사전(딕셔너리)
```
---
### 데이터 타입 출력 
```python
print(type(str1))  # <class 'str'>
print(type(bool1)) # <class 'bool'>
print(type(float1)) # <class 'float'>
print(type(int1)) #<class 'int'>
print(type(list1)) #<class 'list'>
print(type(dict1)) # <class 'dict'>
print(type(tuple1)) # <class 'tuple'>
print(type(set1)) # <class 'set'>
```

### 숫자형 연산자
- +, - , *, / , %, // #
```python
i1 = 30
i2 = 944
big_int1=1232132132132444124124214214124
big_int2=99999994121412414524214124214124124

print (i1+i2)  
print(big_int1 + big_int2) #메모리 허용범위에서 무한대 사용가능 ( 정수 크기 제한 없음)

print(3**4) # 제곱** 81
```
---
### 형 변환
```python
a = 3.
b=10
c=.5
d=12.5
print(type(a), type(b), type(c), type(d))

#정수 -> 실수
print(float(b))

#실수 c -> 정수
print(int(c))

#bool True -> 정수
print(int(True))
print(float(True))
print(int(False))
print(complex(3)) #정수 -> 복소수

#수치 함수
print(abs(-42))  #절대값함수
print(pow(3,4)) #3**4

#type결과는 클래스 객체로 뜸
# 파이썬에서 모든 값은 객체이고, 객체는 어떤 클래스에서 만들어졌는지 정보를 가지고 있다.
```
### Escape 코드
- \n 개행, \t 탭, \\문자, \' ,\000

### 문자열 출력
```python
print('python welcome')
print("python welcome")
print("""python 
      wel
      come""") #여러 줄에 걸쳐 출력할 때 유용
print() #enter
```
---
### 문자열 인덱싱과 슬라이싱
- **인덱싱**이란 무엇인가를 '가리킨다', **슬라이싱**은 무언가를 잘라 낸다라는 의미

```python
str1 = "Python interesting"
print(str1[0:3]) # Pyt
print(str1[:])  #Python interesting
print(str1[:4]) #Pyth 출력
print(str1[4:]) #인덱스 4부터 끝까지
print(str1[:len(str1)]) #인덱스 0부터 문자열의 길이-1
print(str1[1:-2]) #인덱스 1부터 뒤에서 3번째까지
print(str1[-4:-2]) #뒤에서 4번째부터 3번째
print(str1[1:4:2]) #인덱스 1부터 3까지 2까지 점프  yh
```

### 문자열 포매팅 format - c스타일 코드
- %s : 문자열, %c : 문자 1개, %d : 정수, %f : 부동소수, %o : 8진수, %x : 16진수, %% : Literal%(문자 % 자체)
- 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다. -> "Error is %d%%" % 98

```python
# 1. 숫자 바로 대입
print("I eat %d apples." % 3)
# 2. 문자열 바로 대입
print("I eat %s apples." % 'five')
# 3. 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)
# 4. 2개 이상 값 넣기
number = 10
day = "three"
print("I eat %d apples. so I was sick for %s days." % (number, day))
print("%s %s" %('one','two'))
print("%d %d" %(3, 4))
print("%f" %(3.14)) #%f는 소수6자리 기준
 
print("%10s" %("hi"))  #오른쪽정렬
print("%-10s" %("hi")) #왼쪽

a = "I eat {0} apples".format(3)
print(a)  # I eat 3 apples
 
a="I eat {0} apples".format("five")
print(a)   # I eat five apples
```

### format 함수
```python
print("I eat {0} apples".format(3))
print("{} {}" .format('one', 'two'))  # one two
print("{1} {0}" .format('one', 'two'))  # two one
print("{0} {1}" .format(1,2))   #  1 2

print("%10s" %('python')) #10자리에서 오른쪽 정렬로 파이썬 출력
print("{0:>10}".format('python'))   # 오른쪽 정렬

print('%-10s' %('python')) #왼쪽 정렬
print("{0:<10}".format('python'))  #왼쪽 정렬

print("{0:^10}".format('python'))  #가운데 정렬

# 5자리까지 출력(절삭)
print("%.5s" %('pythonjavascript'))
print("%06.2f" %(3.1415921234567)) #총 6개에서 소수점 2자리/ 앞부분으로 0 채워라   -> 003.14

x = 30
y = 50
z = 42032
str1 = "kim"

ex1='%s %f %d' %(str1, z, (x+y))
print(ex1)    # kim 42032.000000 80
print(type(z))  # <class 'int'>

# 공백 채우기
print("{0:_<10}" .format("python"))

```

