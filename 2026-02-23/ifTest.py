#if
print(type(True))
print(type(False))

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

adr=""
if adr:
    print(adr)
else:
    print('주소 뭐야')
adr = "seoul"
if adr:
    print(adr)
else:
    print('주소 뭐야')

a = 85
b = 29
c = 20
print(a>b and b>c)
print(a>b or b>c)
print(not a>b)
print(not b>c)
print(not True)
print(not False)

print(3+2==5 and not 7+3>0)

grade1=90
grade2='A'
if grade1>= 90 and grade2 =='A':
    print('합격')
    print('합격이야~~')
else:
    print('불합격')

#in, not in
x = [10,20,30] #list
y = {70, 80, 90, 100} #set
z={"name":"kim", "city":"seoul", "id":"gildong"} #dict
m=(10, 20, 24) #tuple

print(25 in x)
print(90 in y)
print(20 not in m)
#p.101
print("city" in z)
print("gildong" in z.values()) #값들에 gildong값이 있는지 확인

score = 90
if score>=90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# 중첩 조건문
grade = 'A'
total = 85

if grade == 'A':
    if total>=90:
        print('장학생')
    elif total >= 80:
        pass
    else:
        print('학생')
else: #grade가 A가 아닐 때
    print('다시 시험봐야됨')


#초기 조건 증감
#while 조건:
# 반복할 실행코드

num =5 
while num>0:
    print(num)
    num=num-1

a = ['a', 'b', 'c']

while a: #리스트에 값이 있으므로 True로 인식
    print(a.pop())

n = 10
while n > 0:
    print(n)
    n = n -1
    if n ==2:
        break # 반복문 탈출

n = 10
while n > 0:
    n-=1
    if n==2:
        continue #제외 (n==2 이면 반복문 다시 실행)
    print(n)
print("---------")
i = 1
while i <=10:
    print(i)
    if i ==5:
        break
    i+=1

print("-------------")
n = 10
while n>0:
    n-=1
    print(n)
    if n ==5:
        break
    else:
        print("final")

print("-----------")

a1 = ['water', 'python', 'java', 'phone']
s1 = 'py'
i = 0

# 리스트 끝까지 py랑 같은지 확인하는 코드 -> 같으면 반복문 종료시킴
# while 뒤의 else는 루프가 break 없이 끝났을 때만 실행된다!
# while~else 구문 (while루프가 정상적으로 끝났을 때만 else블록 실행된다. break로 루프가 중간에 종료되면 else실행안된다)
while i < len(a1):
    if a1[i] == s1:
        break
    i+=1
else:
    print("hi")

li=['a', 'b', 'c']
while True: #무한루프 안에서
    if not li: #li리스트에 값이 없으면
        break #반복문 탈출
    print(li.pop()) #li리스트에 값있으면 끝에서부터 출력

#Q1
n=1
while n<=10:
    n += 1
    if n % 2 == 0:
        print(n)
    
# Q2
dic={'name':'tom','age':'11'}

dic['subject'] = 'python'
print(dic)
del dic['name']
print(dic)

# Q3
s1 = set(([1,2,3]))
print(s1)

# Q4
s2 = 'python'
print(list(s2))

# Q5
s4=set([1,2,3,4,5])

s5=set([6,7,3,4,10])   

print(s4 & s5)
print(s4 | s5)

test_list=['one','two','three']
for i in test_list:
    print(i)
# for i in collecton:
# 반복할 실행코드

names=['kim','lee','park','choi']
for i in names:
    print(i)

word = "python"
for d in word:
    print(d)

profile={
    "name":"hong",
    "age" : 33
}

for i in profile:
    print(i) #키값 반환
    print(profile[i])  #Value 값 반환

print("=========================")
for i in profile.values():
    print(i)

fruit = 'pineApple'
for i in fruit:
    if i.isupper():
        print(i)
    else:
        print(i.upper())

num = [34, 62 ,63, 1, 35, 6, 2]
for i in num:
    if i == 35:
        print("35!")
        break
    else:
        print(i)
print("=======================")

#is: 두 객체가 같은 객체(메모리 주소가 같은지) 인지 비교하는 연산자!
li=["3",1,2,True,4.5]
for i in li:
    if type(i) is str:
        continue
    print(i, type(i))



num = [34, 62 ,63, 1, 35, 6, 2]
for i in num:
    if i == 35:
        print("35!")
        break
else:
    print('hihi')

fruit2 = "Mango"
print(reversed(fruit2))   #객체 주소 값
print(list(reversed(fruit2))) #객체 안에 들어있는 값을 실제로 꺼내서 리스트로 만들어줌
print(tuple(fruit2))
print(set(fruit2)) # 순서유지안됨

#range
for i1 in range(10):
    print(i1)

#1~10까지
for i2 in range(1,11):
    print(i2)
#while문 바꾸기

i3 = 1
while i3 <= 10:
    print(i3)
    i3 +=1

print() #enter

for i4 in range(1,11,2): #1~10수 중 2 증가
    print(i4, end= ' ')
print()

#1~10까지의 합
#p.145

sum1=0
for i in range(1,11):
    sum1 =+ i 
print(sum1)

# 구구단
for i in range (2,10):
    for j in range(1,10):
        print('{:5}'.format(i*j),end = ' ') #기본이 오른쪽 정렬
    print() #enter

# p.147 리스트 컴프리헨션
a = [1,2,3,4]
result=list() #[]

for num in a:
    result.append(num*3)
    
print(result)

#Quiz8
msg="It is Time"
for i in range(len(msg)):
    if msg[i].isupper():
        print(msg[i])
    else:
        continue

#Quiz9
for i in range(1,11):
    if i % 2 == 0:
        continue
    else:
        print(i)

#Quiz10
for i in range(1,33):
    if i % 3 == 0:
        print(i)

