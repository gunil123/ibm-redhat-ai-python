str1="Python"
str2='How are you?'
str3 = """Thank you"""
str4 = '''Nice to meet you'''

print(type(str1))
print(type(str2))
print(type(str3))
print(type(str4))

#믄지열 길이
print(len(str1)) 

str5=''
print (type(str5), len (str5))

str6 = str() 
print(type(str6), len(str6)) 

int1=int(5) #5,6을 정수형 객체로 변환

float1=float(4)  #4를 실수형 객체로 형변환
print(float1)

ex_str1 = "Do yuu have a  \"phone\"?"
print(ex_str1)

# p.54
t_str = "Ph \y thon"
print(t_str)


# 문자열 형변환
print(type(str(33)))
print(str(3.4))
print(str(True))

#format사용(%d %s %f %c)
print ("%s %s" %('first', 'second'))
print ("{0} {1}".format('first','second'))

print("%10s" %('python')) #오른쪽정렬
print("{0:>10}.format('python')")

print("%-10s" %('python')) #왼쪽정렬
print("{0:<10}.format('python')")

#10글자에 python * 포함(왼쪽정렬)
print ("{:*<10}".format('python')) 
#10글자에 python * 포함(중앙정렬)
print ("{:*^10}".format('python')) 

#절삭
print("%.3s" %('pythonjava')) #세글자까지만 출력하고 나머지 버림
print("{:.3}".format('pythonjava'))
print("{:10.3}".format('pyhonjava')) #10자리 수 에서 3글자만 나오게 해라

print("%d %d %d" %(2,3,4))

#4자리수에서 정수 12출력 %
print("%4d" %(12))

print('%f' %(1.3232323231231322))
print('%3d' %(12321313221313123))  #12321313221313123
# 최소 3자리 공간을 확보해서 출력해줘
#최대 길이를 제한하는것이 아님
print("%3s" %('pythonjava'))

#p.71
name = '홍길동'
age=30
str1=f'내 이름은 {name}입니다. 나이는 {age}입니다'
print(str1)

name2='홍길동'
age2=20
str2='내이름은 {0} 입니다. 나이는 {1} 입니다'.format(name2, age2)
print(str2)

x=10
y=30
z='Lee'

test1= 'z=%s, sum=%d' %(z, (x+y))
print(test1)
#format 함수
test2='z={z}, sum={sum}'.format(z=z, sum=x+y)
print(test2)

test3 = f'z={z}, sum={x+y}'
print(test3)
#정렬
print(f"{'hello':>10}")

n=50
print(f"{n:<20}")
print(f"{n:>10}")

print(f'{n:-<10}')
print(f'{n:#>20}')

a = "hobby"
print(a.count('b'))

a = "Python is the best choice"
print(a.find('b'))
print(a.find('k')) #-1


a = "Python is the best choice"
print(a.index('b')) #14

result = ",".join('abcd')
print(result)
a = "hi"
print(a.upper()) 

a = " hi "
print(a.lstrip())  
print(a.rstrip())
print(a.strip())  # hi

a = "Life is too short"
print(a.replace("Life", "Your leg")) #Your leg is too short
print(a.split())

a = 'hi'
print(a.upper()) #HI
print(a) #hi


#p.77
list1=[]
list2=list()
print(list1, list2)
print(type(list1),type(list2))


list3=[60,100,98,95]
list4=[1000,1000,'Tom','Juli',"Jack"]
list5=[1000,1000,['Tom','Juli',"Jack"]]
list6=[3.42,'python',3,1,False,3.2212]

# list4 문자열만 추출
list4_strings = [x for x in list4 if isinstance(x, str)]
print(list4_strings)
# list5 안에 있는 리스트에서 문자열만 추출
list5_strings = [x for x in list5[2] if isinstance(x, str)]

# list6에서 문자열만 추출
list6_strings = [x for x in list6 if isinstance(x, str)]

print("list4 문자열:", list4_strings)
print("list5 내부 리스트 문자열:", list5_strings)
print("list6 문자열:", list6_strings)

#인덱싱
print(list4[1])
print(list4[0] + list4[1] +list4[1])
print(list4[-1]) #뒤에서 첫번째 값
print(list5[-1][1]) #뒤에서 첫번째 값 중 ['Tom','Juli',"Jack"] 인덱스 1값

#슬라이싱
print(list4[0:3]) #[1000,1000,'Tom']
print(list4[2:]) #인덱스2부터 끝까지
print(list5[2][1:3])  # ['Tom','Juli',"Jack"]에서 인덱스 1부터 2까지

#연산
print(list3+list4) #리스트 합치기
print(list3*3) #리스트 반복
#print(list3[0]+"hi")
print(str(list3[0])+"hi") #"60" +"hi"
print(list4[2]+"hi")

#수정
list3[0]=4  #4를 list3[0]자리에 넣어
print(list3)

#[4,100,98,95]
list3[1:2]=['a','b','c']
print(list3)  #[4, 'a', 'b', 'c', 98, 95]

list3[1:2]=[]
print(list3) #[4, 'b', 'c', 98, 95]

del list3[3] 
print(list3)

number = 10
day = "three"
print("I eat %d apples. so I was sick for %s days." % (number, day))

a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)
a = [1, 2, 3]
print(len(a))

a = [1, 2, 3]
a[2] = 4
print(a)

del a[1]
print(a)