def qq(a,b): 
    for i in range(a,b):
        print(i)
qq(1,10)

def name(word):
    print(word)
a = "python"
name(a)

def name2(word):  
    n = 'Hi' + (word)
    return n

x = name2('good') #함수의 리턴값이 x에 대입된다
print(x)
#####################

def multi(x):
    y1 = x * 5
    y2 = x * 10
    y3 = x * 20
    return(y1,y2,y3)

a,b,c = multi(10)  #a,b,c=y1,y2,y3
print(a,b,c)

#######

def func1(x):
    y1 = x * 5
    y2 = x * 10
    y3 = x * 20
    return(y1,y2,y3)
a=func1(5) #a의 값은 return 값
print(a, type(a))   # (25, 50, 100) <class 'tuple'>
###########
#a를 list로 변환해서 출력
print(list(a))

def func2(x):
    y1 = x * 5
    y2 = x * 10
    y3 = x * 20
    return[y1,y2,y3]

a = func2(5)
print(a, type(a), set(a))

####################

def func3(x):
    y1 = x * 5
    y2 = x * 10
    y3 = x * 20
    return{'y1':y1,'y2':y2,'y3':y3}

a = func3(5)
print(a, type(a))

print(a['y2'])
# print(a.get('y2'))
print(a.items())
print(a.keys())

# *args
def func1(*args):
    for i in args:
        print(i)
func1('gildong')
func1('gildong', 'tom', 'juli')
func1('gildong', 'tom', 'juli','jack')

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

#초기값 설정
def say(name, man, old=20):
    print(name)
    if man:
        print('남자', old)
    else:
        print("여자", old)
say('jili', True)
say('tom', False, 10)


############
def calcu(name, time, count, price):
    if time == 15 & count >= 3:
        print(f'{name}씨는 10%할인 = {price*0.9}원')
    elif time == 12 * count >=5:
         print(f'{name}씨는 20%할인 = {price*0.8}원')
    else:
        print(f'{name}씨는 할인 없음={price}원')
calcu("형민",15,4,20000)
calcu("종진",12,5,50000)
calcu("한빈",10,2,70000)
 
# p.167
a = 1
def vartest(a):
    a = a + 1
    return a
    
a = vartest(a)
print(a) 

# lambda
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

def final(x, y, func1): #함수를 다른 함수의 매개변수로 넘길 수 있음 -> 고차함수 -> multi가 final의 매개변수로 들어감
    print(x, y , func1(5, 6))

final(1, 2, multi)

#input 함수(기본타입 str)

# name = input('이름은?')
# score = input('학점은?')
# age = input('나이는?')

# print(name,score,age)
# print(type(name), type(score), type(age))

# num1 = int(input('첫번째 정수')) #문자열 타입 -> 숫자(정수)타입으로 변경
# num2 = int(input('두번째 정수'))
# print(num1 + num2)

# a,b=input('숫자입력').split() #p.76
# a=int(a)
# b=int(b)
# print(a+b, type(a+b))

# map(f, iterable) : 함수와 반복가능한 자료형을 입력으로 받는다.
def pp(x):
    return x + 20
print(pp(4))
print(list(map(pp,[1,2,3])))

# 1~5까지 list로 표현
li = [x for x in range(1,6)] 
print(li)
li2= list(range(1,6))
print(li2)

re = list() #re=[]
for i in li2:
    re.append(i)
print(re)

def one(i):
    return i 
#li2 요소를 하나하나 one의 매개변수로 받아 리턴받는다 map함수 이용
re2 = list(map(one,li2))
print(re2)

one = list(map(lambda i:i, li2))
print(one)

list1=[1,2,3,4,5]
#map을 사용해 10씩 증가시킨다(lambda)
re3=list(map(lambda i:i+10 ,list1))
print(re3)

for i in re3:
    print(i)

