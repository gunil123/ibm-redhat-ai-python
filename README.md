# IBM x RED HAT AI과정
## python

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
result = ",".join(letters)
print(result)  #a,b,c,d
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

