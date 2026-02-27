class Mul:
    def __init__(self,m):
        self.m = m

    def __call__(self, n): #객체를 함수처럼 호출할 수 있게 해주는 메소드

        return self.m*n
    
if __name__=="__main__":
    mul3 = Mul(3)
    mul5 = Mul(5)

    print(mul3(10))
    print(mul5(10))

#클로저
#함수 안의 함수를 결과를 반환할 때 (콜백함수, 데코레이터 함수에 사용)

#add 바깥함수 안에 wrapper라는 함수가 안에 있다.(inner fuction)
#내부함수가 바깥함수의 n1을 기억하고 사용할 수 있는 구조로 되어있다(클로저의 특징)
# class Add:
    # def __init__(self, n1):
    #     self.n1=n1
    # def add(self, n):
    #     return self.n1+n
def add(n1):
    def wrapper(n):
        return n1 + n
    return wrapper
a1 = add(10)
print(a1(10))

#a1 = add(10) => n1=10 저장 -> wrapper함수 변환 -> a1에는 wrapper 들어감
#print(a1(10)) => print(wrapper(10)) 실행 -> n1(기억된 10) +10 =20

a2=add(20)
print(a2(10))

# 데코레이터 - 장식하는 도구(기능 확장o)
# 함수에 @기능을 붙인다.

# 클로저를 사용해 데코레이터 구현함
def trace(func):
    def wrapper():
        print('시작')
        func()
        print('끝')
    return wrapper #함수반환
@trace #hi=trace(hi)
def hi():
    print('hi')
@trace
def hello():
    print('hello')

t1 = trace(hi)  #t1 = wrapper / wrapper는 hi(func)를 기억하고있다.
t1()  #wrapper()
t2 = trace(hello) #t2=wrapper
t2()

def trace(func): #p.160,161
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(args, kwargs, result)
        return result
    return wrapper

# t = trace(10,20)
# t()
######################
def trace(func): #p.160,161
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(args, kwargs, result)
        return result
    return wrapper
@trace
def big(*args): #2. wrapper(10,20) 실행 -> result=max(10,20) => 20반환
    return max(args)
@trace
def mini(**kwargs):
    return min(kwargs.values())
print(big(10,20))
print(mini(x=2,y=30,z=40))

class Tr:
    def __init__(self,func):
        self.func=func
    def __call__(self): #인스턴스를 함수처럼 호출 가능
        print(self.func.__name__, "시작")
        self.func()
        print(self.func.__name__, "끝")

#클래스형 데코레이터
#@데코레이터 : 함수, 인스턴스로 바꿔주는 문법
#hi = Tr(hi)
@Tr   #Tr클래스의 __init__에 hi를 전달해줘.. ->func의 값이 hi가 되면서 hi는 함수가 아니라 Tr의 인스턴스
def hi():
    print("hi")
hi() #hi는 인스턴스가 되었다. 인스턴스를 함수처럼 썼기 때문에 __call__자동호출됨

it = [1,2,3,4,5].__iter__()

print(next(it))
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())


class Cnt:
    def __init__(self,stop):
        self.current = 0
        self.stop= stop

    def __iter__(self):    #iter(obj) -> 이터레이터 객체 만듬
        return self
    
    def __next__(self): #next(obj) -> 반환된 이터레이터 객체에 next()반복호출
        if self.current < self.stop:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration #예외 강제발생

#c = Cnt(5)
# for 문이 객체를 받을 때 자동으로 __inter__호출

for i in Cnt(5):
    print(i)

for i in range(3,4):
    print(i)

#generator : 이레이터 생성해주는 함수(yield 키워드)
# 발생자 -> 메모리 절약, 속도 효율성, 문법 간결

num2 = [i*2 for i in range(1000000)]

def get():
    for i in range(1,1000000):
        yield i * 2
g = get()
print(next(g))

def gen1():
    yield 0  #0을 함수 밖에 전달하면서 코드 실행을 함수 밖에 양보함
    yield 1
    yield 2

# yiled를 사용해 바깥을 전달한 값은 next 함수의 반환값으로 나온다
g1 = gen1()
a = next(g1)
print(a)

b= next(g1)
print(b)

c = next(g1)
print(c)

for i in gen1():  
    print(i)

def num1(stop):
    n = 0
    while n < stop:
        yield n 
        n += 1

for i in num1(3):
    print(i)

def gen(x):
    for i in x:
        yield i.upper()

xy = ['apple', 'pineapple', 'banana']

for i in gen(xy):
    print(i)

import asyncio

# 코루틴(coruotine)
async def show(name, sec):
    print("start")
    await asyncio.sleep(sec)
    print("final")

async def main():
    li=[ show('python',2), show('java',3) ]
    await asyncio.gather(*li)
    # await asyncio.gather(  #두 개 작업이 다 완료될때까지 기다린다./show함수 동시시작
    #     show('python',2), 
    #     show('java', 3)
    #)
# 1. show함수 동시에 실행
# 2. 2초 후에 python 작업이 완료됨 show('python',2) -> final
# 3. 3초 후에 java 완료됨 show('java',3)
# 동기식이면 5초걸리는데, 비동기 방식으로 해서 3초걸림
asyncio.run(main())

# 스레드 vs 비동기 차이
## 여러파일 동시에 다운로드 vs 다운로드 도중 다른 작업처리
