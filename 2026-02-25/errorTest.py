#예외처리
#SyntaxError, NameError, IndexError, ZeroDivisionError, KeyError, ValueError, TypeError....

# print('h) 
# print('h')) #SyntaxError

# x=3
# y=4
# print(z) #NameError

# a=[1,2,3]
# print(a[5])  #IndexError

# print(4/0)   #ZeroDivisionError

# a={'a':'gg','b':33}
# print(a['b'])
# print(a['c'])  #KeyError

# x=[1,2,3]
# x.remove(2)
# x.remove(5) #ValueError

x = [1,2]
y = 'python'
#print(x + y) #TypeError
print(x + list(y))

li = ['db', 'python', 'react']
try: #예외가 날 수도 있는 코드 출력
    x = 'java'
    y = li.index(x) #예외발생 하자마자 except 절로 넘어감
    print('try 블럭 수행')
except ValueError: #예외 발생할 때 실행되는 블럭
    print('except 블럭 수행')

else: #예외 없을 때 실행되는 블럭
    print('except 블럭 수행')

##################################


li = ['db', 'python', 'react']
try: #예외가 날 수도 있는 코드 출력
    x = 'java'
    y = li.index(x) #예외발생 하자마자 except 절로 넘어감
    print('try 블럭 수행')

except Exception as e: #예외 발생할 때 실행되는 블럭
    print(e)
else: #예외 없을 때 실행되는 블럭
    print('else')
finally: #무조건 실행되는 블럭(예외발생여부 상관없음)
    print("finally")

print("-----------------------------------")

#Exception 클래스 상속받음
class MyError(Exception):
    def MyError(Exception):
        super().__init__('허용되지 않는 별명입니다')
def say_nick(nick):
    if nick == '바보':
        raise MyError()  #예외를 일부러 발생시킴
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')

except MyError as e:
    print(e)


