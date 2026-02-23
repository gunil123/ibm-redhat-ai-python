#함수
#개발자가 함수명 통해서 정의한 후에 필요할 때마다 호출
#반복되는 코드를 한번 구현 한후 재사용 가능하도록 만든 코드의 집합
#함수 구현 후 -> 재사용

#매개변수가 있는 함수
#매개변수가 업는 함수
#결과값 반환하는 함수(return)
#결과값 반환 안하는 함수

def func1(): #매개변수가 없는 함수
    print("함수1")
#함수 호출 -> 함수실행
func1()

def func2(a,b): #매개변수가 있는 함수
    print(a,b) #결과값 반환 안하는 함수

func2(1,2)

def func3(a,b): #매개변수가 있는 함수
    return(a+b)  #결과값 반환하는 함수(return)

print(func3(10,20))

###########
a = [1,2,3,4]
result=[num*2 for num in a] #[변수 for 변수 in collection]
print(result)

#3~30까지 출력 -> list
b = [i for i in range(3,31)]
print(b)

#3~30까지 출력 3의 배수만 -> list
b2=[i for i in range(3,30) if i % 3 == 0]
print(b2)

#1~10까지 -> list
b3 = [i for i in range(1,11)]
print (b3)

# p.148
result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)