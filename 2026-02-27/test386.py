# Q1.
s = "a:b:c:d:"
s1=s.split(':')
print("#".join(s1))

# Q2.
a = {'A':90, 'B':80}
a['C'] = 100
print(a['C'])

# Q3.
a = [1, 2, 3]
print(id(a))  #1589928553600
a = a + [4, 5]
print(a)   
print(id(a)) #1589928555264

a = [1, 2, 3]
print(id(a))   #1589928651584
a.extend([4, 5])
print(a) 
print(id(a))   #1589928651584

# -> 리스트에 +를 사용하면 a가 저장되있는 다른 주소 값을 리턴하고, extend를 사용하면 그대로 유지되는 것을 알 수 있다.  

# Q4. 
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum2 = 0
for i in A:
    if i > 50:
        sum2 += i
print(sum2)

# Q5. 피보나치 함수

n = int(input('정수를 입력하시오 : '))

def fib(n):
    if n == 0 : return 0
    if n == 1 : return 1
    return fib(n-2) + fib(n-1)
for i in range(n):
    print(fib(i), end = " ")
print(' ')


# Q6. 숫자의 총합 구하기
s = input('숫자를 입력하세요 : ')
n1 = s.split(",")
result = 0
for i in n1:
    result += int(i)
print(result)

# Q7. 한줄 구구단
g = int(input('구구단을 출력할 숫자를 입력하세요(2~9) : '))

for j in range(1, 10):
    print(g * j, end = " ")



# Q8.
f = open('abc.txt', 'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open('abc.txt', 'w')
for line in lines:
    line = line.strip()
    f.write(line)
    f.write('\n')
f.close()

#Q9. 평균값 구하기
with open('sample.txt', 'w') as f:
    f.write('70\n60\n55\n95\n90\n80\n80\n85\n100\n')

with open('sample.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

total = 0
for line in lines:
    score = int(line)
    total += score
average = total / len(lines)

with open('result.txt', 'w') as f: 
    f.write(str(average))

# Q10. 계산기 만들기
class Calculator:
    def __init__(self, *args):
        self.numbers = args

    def sum3(self):
        return sum(self.numbers)
       
    def avg(self):
        return sum(self.numbers)/len(self.numbers)
        

cal1 = Calculator(1, 2, 3, 4, 5)
print(cal1.sum3())
print(cal1.avg())

cal2 = Calculator(6, 7, 8, 9, 10)
print(cal2.sum3())
print(cal2.avg())
# arg로 튜플로 묶어 내장함수 처리

# Q11. 모듈을 사용하는 방법
import sys
sys.path.append("c:\\doit")
import mymod
print(mymod.add(3,4))
# doit 디렉터리를 추가하고, mymodule을 만들어 사용

#Q12. 오류와 예외처리
result = 0
try : 
    [1, 2, 3,][3]
    "a" + 1
    4 / 0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError:
    result += 3
finally:
    result += 4
print(result)
# 7, IndexError 발생 -> finally = 0 + 3 + 4 = 7

# # Q 13. DashInsert 함수
# data = "4546793"
# numbers = list(map(int, data))
# result = []
# for i, num in enumerate(numbers):
#     result.append(str(num))   
#     if i < len(numbers)-1:  # 다음 수 있으면
#         is_odd = num % 2 == 1  #현재 수 홀수
#         is_next_odd = numbers[i+1] % 2 == 1  # 다음 수 홀수
#         if is_odd and is_next_odd:  #연속 홀수
#             result.append("-") #-추가
#         elif not is_odd and not is_next_odd:
#             result.append("*")   # *추가
# print("".join(result))

# # Q 14. 문자열 압축하기
# def compress_string(s):
#     _c = ""
#     cnt = 0
#     result = ""
#     for c in s:
#         if c!=_c:
#             _c = c
#             if cnt: result += str(cnt)
#             result += c
#             cnt = 1
#         else:
#             cnt += 1
#     if cnt: result += str(cnt)
#     return result
# print(compress_string("aaabbcccccca"))

# # Q 15. Duplicate Numbers 함수
# def dup_numbers(s):
#     result = []
#     for num in s:
#         if num not in result:
#             result.append(num)
#         else:
#             return False
#     return len(result) == 10

# print(dup_numbers("0123456789"))
# print(dup_numbers("012345"))
# print(dup_numbers("01234567890"))
# print(dup_numbers("6789012345"))
# print(dup_numbers("0213224567689"))