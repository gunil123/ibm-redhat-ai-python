# Q3.
print(all([1, 2, abs(-3)-3]))
 #-> Flase
print(chr(ord('a')) == 'a') # -> True

# Q4.
print(list(filter(lambda x : x>0 , [1, -2, 3, -5, 8, -3])))

#Q7.
# print(max([-8,2,7,5,-3,5,0,1]) + min([-8,2,7,5,-3,5,0,1]))

a = [-8,2,7,5,-3,5,0,1]
print(max(a) + min(a))

#Q8.
a = 17 / 3
print(round(a, 4))

#Q11.
import time
print(time.strftime('%Y-%m-%d %H:%M:%S'))
#Q12.
import random
result = []
while len(result) < 6:
    num = random.randint(1,45)
    if num not in result:
        result.append(num)
print(result)

result = set()
while len(result) < 6:
    result.add(random.randint(1, 45))
print(result)
#Q17.
import random

human =  ['김승현', '김진호', '강춘자', '이예준', '김현주']
do = ['청소', '빨래', '설거지', '휴식', '휴식']

random.shuffle(human)
for i in range(5):
    print(f"{human[i]} : {do[i]}")


# Cafe-Q1.
# 생성자: 이름, 초기금액
# deposit() : 입금
# withdraw() :출금
# show_balance() : 현재 잔액 보이기
# 출금 시 잔액 부족 시 "잔액이 부족하다" 출력
# 객체 생성코드 참고
# acc1 = Account("홍길동", 10000)
# acc1.show_balance()  -> 홍길동님의 현재 잔액 10000원
# acc1.deposit(5000)  -> 현재 금액+5000 원 더하기
# acc1.withdraw(3000) -> 현재 금액 - 3000
# acc1.withdraw(20000) # 잔액 부족
# acc1.show_balance()  -> 홍길동님의 현재 잔액 {}원
