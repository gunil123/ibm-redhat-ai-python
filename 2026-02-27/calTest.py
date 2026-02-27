#Q1
def calc(oper, *args):
    if oper == "add":
        return sum(args)

    elif oper == "mul":
        multi = 1
        for i in args:
            multi *= i
        return multi
    elif oper == "avg":
        return sum(args)/len(args)
    else:
        raise ValueError('잘못된 연산이다')
print(calc("add", 1,2,3)) #6
print(calc("mul", 1,2,3,4)) # 24
print(calc("avg", 10,20,30)) # 20

# #Q2. 
# #사용자 정의 예외(예외를 만듬)
# class AgeError(Exception):
#     pass

# try:
#     age=int(input('나이 입력'))

#     if(age<=0):
#         raise AgeError('나이는 0이상이어야해')
    
#     print('입력 완료')

# except ValueError:
#     print('숫자 입력해야돼!')

#Q3.
class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.id}, {self.name}, {self.email}"
    
class UserManager:
    def __init__(self):
        self.user = []
    def add_user(self, user):
        self.user.append(user)

    def delete_user(self, user_id):
        self.user = [i for i in self.user if i.id!=user_id]    
    
    def li_user(self):
        for i in self.user:
            print(i)
    
    def find_user(self, user_id):
        for i in self.user:
            if i.id == user_id:
                return i
        return None

user1 = User(1, "홍길동", "hong@aa.com")
user2 = User(2, "김길동", "kim@aa.com")
user3 = User(3, "박길동", "park@aa.com")

manager = UserManager()
manager.add_user(user1)
manager.add_user(user2)
manager.add_user(user3)

find_id = 2
result = manager.find_user(find_id)

if result:
    print

manager.li_user()
print("=================")
manager.delete_user(1)
manager.li_user()


#Q4.
#무한대로 짝수를 생성해라
def even_gen():
    n = 0
    while True:
        yield n
        n += 2

g = even_gen()
print(next(g))
print(next(g))
print(next(g))

#Q5.
# 파일 처리

def score1(name, score):
    try:
        with open('score1.txt', 'a', encoding='utf-8') as f:
            f.write(f"{name},{score}\n")      
        print(f"{name}님의 데이터가 메모장에 읽기 좋게 저장되었습니다.")
    except ValueError:
        print("점수는 숫자로 입력하세요")

def average():
    sum=0
    cnt=0
    try:
        with open('score1.txt', 'r', encoding='utf-8') as f:
            for i in f:
                i=i.strip()
                name,score=i.split(",")
                sum+=int(score)
                cnt+=1
        return sum/cnt       

            
    except FileNotFoundError: 
        print("파일이 없습니다.")
        return None

# 실행
score1('홍길동', 100)
score1('김길동', 150)

avg=average()
print(avg)

#Q6.
login_state=False

def login(func):
    def wrapper(*args, **kwargs):
        if not login_state:
            print('로그인')
            return
        return func(*args, **kwargs)
    return wrapper
@login #데코레이터함수
def write_post():
    print("글 작성 완료")
write_post()   #로그인
login_state = True
write_post() #로그인

#write_post 함수에 @login 데코레이터 적용시킴 -> wrapper()실행됨

