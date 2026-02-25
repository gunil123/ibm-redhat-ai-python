class Car:
    #p.205 
    def __init__(self, make, model, year): #생성자 호출하는 인스턴스 메소드
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0 #Car객체의 속성 speed를 선언하여 초기화
    
    def name(self):
        names=str(self.year) + " " + self.make + " " + self.model
        return names
    
    def speed1(self):
        print(str(self.speed) + "이다")

#객체명 = 클래스명(init함수의 매개변수)
#객체생성코드 -> 자동으로 __init__호출
c1=Car('tesla','models',2018)
print(c1.name())  #인스턴스를 통해 호출하면 파이썬이 자동으로 인스턴스를 self에 넣어줌
c1.speed1()

      

# object(클래스 상속받음)

c1=Car('tesla','models',2018)
print(c1.name())  #인스턴스를 통해 호출하면 파이썬이 자동으로 인스턴스를 self에 넣어줌
c1.speed1()

class A:
    def add(a, b):
        print(a+b)
    def minus(a, b):
        print(a-b)
#객체생성코드
# a1=A()
# a1.add(3,4) #a라는 인스턴스를 받을 self가 없음 
# # TypeError: A.add() takes 2 positional arguments but 3 were given

A.add(3, 4)
A.minus(5, 3)

class Student:
    def __init__(self, id, name, score = 0):
        self.id = id
        self.name = name
        self.score = score

    def getId(self):
        return self.id
    def getNum(self):
        return self.name
    def setScore(self, score):
        self.score = score
    def getScore(self):
        return self.score

class Cal:
    def __init__(self):
        self.stu= []
    def add(self, student):
        self.stu.append(student)

    def avg(self):
        sum = 0
        for i in self.stu:
            sum += i.getScore()
        average = sum/len(self.stu)
        return average, len(self.stu)
a = Student(1, "민구")
a.setScore(100)

a2=Student(2,"덕현",score=90)
a3=Student(3,"유민",score=80)
a4 = Student(4, "상민", score = 80)

c = Cal() #self.stu[]
c.add(a)  #self.stu=[a,a1,a2,a3]
c.add(a2)
c.add(a3)
c.add(a4)

print('평균:{}'.format(c.avg()))

#p.208
#class 자식 클래스명=서브클래스명(부모클래스명=슈퍼클래스 명)
class Person:
    def __init__(self):
        print('안녕')

class Student(Person):
    def __init__(self):
        print('학생은 공부해')
        # 상속받았다 해서 부모 __init__을 자동으로 호출해주지 않는다.
        # super().__init__으로 명시해야 부모클래스의 함수 호출된다. 
        super().__init__()
p=Person()
s=Student()

class Super:
    def a(self):
        print('super')
class Sub(Super):
    def a(self):
        print('자식클래스') #오버라이딩
    def b(self):
        print('sub')
s = Sub()
s.a()
s.b()

s1 = Super()
s1.a()
# s1.b() 부모는 자식 메서드에 접근 불가

#######

#p.208
class Car:
    def __init__(self,make,model,year): #생성자 호출하는 인스턴스 메소드
        self.make=make
        self.model=model
        self.year=year
        self.speed=0 #Car객체의 속성 speed를 선언하여 초기화함

    #인스턴스메소드는 첫번째 인자로 항상 self가 있어야함
    def name(self):
        names=str(self.year) + " " +self.make + " " +self.model
        return names
    def speed1(self):
        print(str(self.speed) + "이다")

class CampingCar(Car):
    def __init__(self, make, model, year, bed):
        super().__init__(make, model, year) # 부모 클래스에 있는 __init__호출
        self.bed = bed
#객체 생성
camp1=CampingCar('tesla','modles',2017, 2)
print(camp1.name())
camp1.speed1()

c1=Car('audi', 'mo',2010)
print(c1.name())
c1.speed1()

class Container:
    stock_num = 0 #클래스 변수(모든 객체가 공유가능) => 클래스명.변수
    
    def __init__(self,name):
        self.name = name #인스턴스 변수(각 객체마다 별도로 저장됨) => 객체.변수
        Container.stock_num += 1
c = Container('Lee')
c2 = Container('Kim')

print(Container.stock_num)
print(c.stock_num)
print(c2.stock_num) 
print(c.__dict__) #파이썬의 특수 속성
print(c2.__dict__)