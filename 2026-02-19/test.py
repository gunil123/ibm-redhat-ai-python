# #파이썬 자료형
# ```
# int 정수
# float 실수
# complex 복소수
# bool 불린
# str 문자열
# list 리스트
# tuple 튜플
# set 집합
# dict 사전(딕셔너리)
# ```

# 데이터 타입
str1="Python"
bool1=True
float1=10.4
int1=3
list1=[str1]
dict1={"name":"gindong","id":3}
tuple1=4,2,4
set1={1,23,4}

# 데이터 타입 출력
print(type(str1))  # <class 'str'>
print(type(bool1)) # <class 'bool'>
print(type(float1)) # <class 'float'>
print(type(int1)) #<class 'int'>
print(type(list1)) #<class 'list'>
print(type(dict1)) # <class 'dict'>
print(type(tuple1)) # <class 'tuple'>
print(type(set1)) # <class 'set'>

#str1 = "Python"
#str1이라는 문자자체를 객체로 만들고 다양한 속성(변수), 행동(함수)를 넣을 수 있다.

# 숫자형 연산자
# +, - , *, / , %, // #
i1 = 30
i2 = 944
big_int1=1232132132132444124124214214124
big_int2=99999994121412414524214124214124124

print (i1+i2)
print(big_int1 + big_int2) #메모리 허용범위에서 무한대 사용가능 ( 정수 크기 제한 없음)

print(3**4)

f1=1.234
f2=3.458
print(f1+f2)
print(f1-f2)
print(f1*f2)
print(f1/f2)

#형 변환
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
"""
Escape 코드
\n 개행
\t 탭
\\문자
\'
\000
"""
#문자열 출력
print('python welcome')
print("python welcome")
print("""python 
      wel
      come""") #여러 줄에 걸쳐 출력할 때 유용
print() #enter

#type결과는 클래스 객체로 뜸
# 파이썬에서 모든 값은 객체이고, 객체는 어떤 클래스에서 만들어졌는지 정보를 가지고 있다.
str1 = "Python interesting"
print(str1[0:3]) # Pyt
print(str1[:])  #Python interesting
print(str1[:4]) #Pyth 출력
print(str1[4:]) #인덱스 4부터 끝까지
print(str1[:len(str1)]) #인덱스 0부터 문자열의 길이-1
print(str1[1:-2]) #인덱스 1부터 뒤에서 3번째까지
print(str1[-4:-2]) #뒤에서 4번째부터 3번째
print(str1[1:4:2]) #인덱스 1부터 3까지 2까지 점프  yh

#format - c스타일(%s - 문자열, %f : 실수, %d: 정수)
print("%s %s" %('one','two'))
print("%d %d" %(3, 4))
print("%f" %(3.14)) #%f는 소수6자리 기준
 
print("%10s" %("hi"))
print("%-10s" %("hi"))

a = "I eat {0} apples".format(3)
print(a)

a="I eat {0} apples".format("five")
print(a)

print("%d %d" %(4,6))

#format 함수
print("I eat {0} apples".format(3))
print("{} {}" .format('one', 'two'))
print("{1} {0}" .format('one', 'two'))
print("{0} {1}" .format(1,2))

print("%10s" %('python')) #10자리에서 오른쪽 정렬로 파이썬 출력
print("{0:>10}".format('python'))   

print('%-10s' %('python'))

# 5자리까지 출력(절삭)
print("%.5s" %('pythonjavascript'))
print("%06.2f" %(3.1415921234567)) #총 6개에서 소수점 2자리/ 앞부분으로 0 채워라

x = 30
y = 50
z = 42032
str1 = "kim"

ex1='%s %f %d' %(str1, z, (x+y))
print(ex1)
print(type(z))

print("%20s" %('script'))
print("{0:>20}".format('script'))

#왼쪽 정렬, 10자리로 바꾸기
# 서식문자, format
print("%-10s" %('script'))
print("{0:<10}" .format("script"))
#10자리 python 왼쪽정렬(자리남으면 _로 채워라)-공백 채우기
#python 문자 10자리 중앙
print("{0:_<10}" .format("python"))
print("{0:^10}" .format('python'))

#116p Q3
pin = "881120-1068234"
yyyymmdd = "19" + pin[0:6]
num = pin[7:8] 
print(yyyymmdd)
print(num)

#116p Q4
pin = "881120-1068234"
num = pin[7]
print(num)
