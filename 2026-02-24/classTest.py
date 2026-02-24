# class 설계도
# object 설계도를 바탕으로 실제 만들어진 제품

# 클래스
# self, 인스턴스 메소드, 인스턴스 변수
# 클래스 메소드, 클래스 변수

#객체(object) : 클래스의 인스턴스를 포함한 모든 파이썬 데이터 //123,"Hello",[1,2,3]
#인스턴스(instance) : 특정 클래스에 의해 생성된 객체를 지칭할 때
from copy import copy
class Profile:
    names="gildong" #클래스 변수(클래스 블록 안 - 모든 인스턴스 접근가능(공유))



    #초기화 함수(self:객체 자기자신)
    def __init__(self, name, age): #인스턴스 변수 : 각 인스턴스마다 개별적으로 존재
        self.name=name  #self를 안적으면 지역변수임 => 인스턴스에 저장되질 않음
        self.age = age

p = Profile("gilding", 13)  #Profile클래스의 인스턴스, 객체가 생성되면 __init__함수 자동 호출됨
p2 = Profile("jiji", 23)

# p, p2 -> Profile 클래스의 인스턴스 / 객체

print(p==p2)
print(id(p), id(p2))

print('{0} {1} {2} {3}'.format(p.name, p.age, p2.name, p2.age))

print(p.names)   # gildong
print(p2.names) # gildong

# p.112, 144
c = p  #같은 주소(주소 동일)
print(p==c, id(p), id(c))

c = copy(c) #p객체의 겉만 복사한 새로운 객체
print(p==c, id(p), id(c))


print("----------------------------------------")
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
