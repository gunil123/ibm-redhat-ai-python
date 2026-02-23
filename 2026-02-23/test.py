# 집합
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

set1 = set([1,2,3,4,5,6])
set2 = set([4,5,6,7,8,9])

print(set1&set2)
print(set1.intersection(set2))

print(set1|set2) #요소 중복 제거되면서 합쳐짐
print(set1.union(set2))

print(set1-set2) #{} set1에는 있지만 set2에 없는 요소들
print(set1.difference(set2))

#중복 요소 확인(두 집합에 공통 요소 없으면 true, 있으면 false)
print(set1.isdisjoint(set2)) #공통요소 4,5,6 있음

#부분집합 set1의 모든 요소가 set2에 있는지 확인
print(set1.issuperset(set2))

a = set([1,2,3,4]) # a = {1,2,3,4}
a.add(5)
print(a)

a.remove(2)
print(a)

#a.remove(6) #없는 값 삭제 -> keyError
#print(a)

a.discard(3)
print(a)

a.clear() #다 제거(요소만 사라진다. 구조만 남아있음)
print(a)

a.update([1,2]) #값 여러개추가 
print(a)

a = [1,2,3]
#a는 리스트 [1,2,3]이 저장되어 있는 메모리 주소값 가지고 있다(reference)
print(id(a))

n = 100
print(type(n))
print(id(n))

# 동시 변언 선언가능
a=b=c=d=100

n=50    #값 덜어씀
print(n)

a = 3
print(id(3))
print(id(a))

b = a
print(id(b))

#p.114
#from 모둘명 import 함수
from copy import copy
a2=[1,2,3] #복사를 했지만 요소만 복사/ 주소값은 복사하지않음/두 주소값이 틀림
b2 = copy((a2))  

x = 3
y= 5
x,y =(y,x) #언팩킹
print(x)
print(y)


age=20

name="에릭"

score='A'

sight=0.5

str = f'{name}은 {age}살의 {sight}시력이며 학점은 {age}이다'
print(str)

print("{}은 {}살의 {}시력이며 학점은 {}이다" .format('에릭', 20, 0.5, 'A'))
names = ['찰스','스누피''루피']
print(f'{names[0]}는 파이썬 배워요')
