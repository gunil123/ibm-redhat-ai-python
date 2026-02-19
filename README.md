# IBM x RED HAT AI과정
## python

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
```
