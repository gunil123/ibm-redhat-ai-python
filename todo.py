import pickle
import re
import os

check1=re.compile('[1-9][_][1-9]')
check2=re.compile('[1-9][_][1-2]\d')
check3=re.compile('[1|3|5|7|8][_][3][0-1]')
check4=re.compile('[4|6|9|][_][3][0]')
check5=re.compile('[1][0-2][_][1-9]')
check6=re.compile('[1][0-2][_][1-2]\d')
check7=re.compile('[1][0|2][_][3][0-1]')
check8=re.compile('[1][1][_][3][0]')

TODO_DB_PATH = "test.obj"
lastId = ""

#Todo 클래스 {"date" : ["content1", "content2"]} 구조
class Todo():
    def __init__(self, date, content): 
        self.date = date
        self.content = content

#test.obj 파일 열어서 반환하는 함수
#print(loadDB()) -> 파일 내용 전부 출력
def loadDB():
    if not os.path.exists(TODO_DB_PATH):
        print("\n[Notice] 저장된 파일이 없습니다. 빈 데이터를 반환합니다.")
        return {}
    
    try:
        with open("test.obj", "rb") as f:
            data = pickle.load(f)
            return data
    except (EOFError, FileNotFoundError):
        print("파일이 비어있거나 찾을 수 없습니다.")
        return {}

#test.obj 파일에 기존 데이터 무시하고 덮어씌우는 함수
def saveDB(db):
    try:
        with open(TODO_DB_PATH, "wb") as f:
            pickle.dump(db, f)
        print("\n[Success] 파일 저장이 완료되었습니다. (내보내기)")
    except Exception as e:
        print(f"\n[Error] 저장 중 문제가 발생했습니다: {e}")


# 전체 삭제 함수
def deleteAll(db):
    # 사용자 확인 입력
    confirm = input("정말 전체 삭제하시겠습니까? y/n : ")
    
    if confirm == "y":
        db.clear()        # 딕셔너리 전체 삭제
        saveDB(db)        # 삭제된 상태를 파일에 저장
        print("전체 삭제가 완료되었습니다.")
    else:
        print("취소 되었습니다.")


# 날짜 단위 삭제 함수
def deleteDate(db):
    # 삭제할 날짜 입력
    date = input("삭제할 날짜를 입력해주세요. : ")
    
    if date in db:        # 해당 날짜가 존재하면
        del db[date]      # 해당 날짜 데이터 삭제
        saveDB(db)        # 변경사항 저장
        print("날짜 삭제가 완료되었습니다.")
    else:
        print("해당 날짜가 존재하지 않습니다.")

# 개별 항목 삭제 함수
def deleteItem(db):
    # 삭제할 날짜 입력
    date = input("삭제할 날짜를 입력해주세요. : ")
    
    if date in db:
        print("현재 목록 :", db[date])  # 해당 날짜의 내용 출력
        
        # 삭제할 내용 입력
        content = input("삭제할 내용을 입력해주세요. : ")
        
        if content in db[date]:
            db[date].remove(content)  # 리스트에서 해당 항목 제거
            
            # 만약 해당 날짜에 내용이 하나도 없으면
            if len(db[date]) == 0:
                del db[date]  # 날짜 자체도 삭제
            
            saveDB(db)  # 변경사항 저장
            print("개별 삭제가 완료되었습니다.")
        else:
            print("해당 내용이 존재하지 않습니다.")
    else:
        print("해당 날짜가 존재하지 않습니다.")

#로그인 진행
def Login(id, pw):
    while True:
        idLogin = input("아이디 입력 : ")
        pwLogin = input("비밀번호 입력 : ")

    #로그인 성공
        if(id == idLogin and pw == pwLogin):
            todoMain(id)
            break

    #로그인 실패
        else:
            print("로그인 실패")
            print("다시 입력하세요")

#회원가입 진행
def User():
    global lastId
    while True:
        id = input("아이디 생성 : ")
        if (id == lastId):
            continue
        else:
            lastId = id
            break

    while True:
        pw = input("비밀번호 생성 : ")
        repw = input("비밀번호 재확인 : ")

    #재확인 성공
        if(pw == repw):
            print('회원가입 성공')
            Main(id,pw)
            break
    #재확인 실패
        else:
            print("회원가입 실패")
            print("비밀번호가 일치하지 않습니다")

    
#메인창
def Main(id,pw):
    while True:
        print("[1] 회원가입 | [2] 로그인")
        print("어디로 이동할까요?")
        userinput = input(": ")
        if (userinput == "1"):
            print("회원가입 진행")
            User()
            break
        elif(userinput == "2"):
            Login(id, pw)
            break
        else:
            print("\n[Notice] 올바른 숫자를 입력해주세요!\n")


def todoMain(id):
    while True:
        print(f"\n========= {id}님, 환영합니다! =========")
        print("[1] 할 일 목록\n[2] 할 일 추가\n[3] 할 일 수정\n[4] 할 일 삭제\n[5] 목록 관리\n[6] 종료")
        print("어디로 이동할까요?")
        userinput = input(": ")
        if(userinput == "1"):
            db = loadDB()
            viewMenu(db)
        elif(userinput == "2"):
            makeTodo()
        elif(userinput == "3"):
            print(list(loadDB().keys()))
            print("\n어느 날짜의 할 일을 선택하시겠습니까?")
            date = input(": ")
            todoUpdate(date)
            break
        elif(userinput == "4"):
            deleteMenu()
        elif(userinput == "5"):
            manageMenu()
        elif(userinput == "6"):
            print("\n======== 이용해주셔서 감사합니다 ========")
            break
        else:
            print("\n[Notice] 올바른 숫자를 입력해주세요!")


""" ----- 할 일 목록 출력 ----- """
def viewAll(db):
    if not db:
        print("\n[Notice] 등록된 할 일이 없습니다.")
        return

    print("\n========= [전체 할 일 목록] =========")
    for date in sorted(db.keys()):
        tasks = ", ".join(db[date])
        print(f"▶ 날짜: {date} | 할 일: {tasks}")
    print("=====================================")

def viewByDate(db, target):
    if target in db:
        print(f"\n--- {target} 할 일 목록 ---")

        tasks = db[target]
        for task in tasks:
            print("-", task)
    else:
        print("\n[Notice] 해당 날짜에 등록된 할 일이 없습니다.")

def viewMenu(db):
    print("\n[1] 전체 보기 | [2] 날짜별 보기")
    print("어디로 이동할까요?")
    choice = input(": ")
    
    if choice == "1":
        viewAll(db)
    elif choice == "2":
        if len(db) == 0:
            print("\n[Notice] 등록된 데이터가 없습니다.")
        print("\n조회할 날짜를 입력하세요 ex) 2_27")
        target = input(": ")
        viewByDate(db, target)
    else:
        print("\n[Notice] 잘못된 입력입니다.")


""" ------ 할 일 추가 ----- """
def addTodo(todo):
    db = loadDB()
    db.setdefault(todo.date,[]).append(todo.content)
    saveDB(db)

def makeTodo():
    while True:
        while True:
            print("\n언제 해야 할 일인가요? ex) 2_27")
            date=input(": ")
            if len(date) == 3:
                if check1.match(date) != None:
                    break
                else:
                    print('\n올바른 날짜를 입력하세요.\n')
            elif len(date) == 4:
                if check2.match(date) != None or check3.match(date) != None or check4.match(date) != None or check5.match(date) != None:
                    break
                else:
                    print('\n올바른 날짜를 입력하세요.\n')
            elif len(date) == 5:
                if check6.match(date) != None or check7.match(date) != None or check8.match(date) != None:
                    break
                else:
                    print('\n올바른 날짜를 입력하세요.\n')
            else:
                print('\n올바른 날짜를 입력하세요.\n')

        print("할 일을 입력해주세요.")
        content = input(": ")
        todo = Todo(date,content)
        addTodo(todo)

        while True:
            print("\n할 일을 더 등록하시겠습니까? y/n")
            more = input(": ")
            if more == 'y' or more == 'n':
                break
            else:
                print('\n[Notice] 올바른 답변을 입력하세요.\n')
                continue
        if more == 'y':
            continue
        else:
            break

""" ----- 할 일 수정 ----- """
def todoUpdate(key):
    global lastId
    db = loadDB()
    oldList = db[key]
    while True:
        viewByDate(db, key)
        idx = 0
        try:
            print("어느 항목을 수정하시겠습니까?")
            idx = int(input("(숫자로 입력): "))-1
            
            if idx < 0:
                raise ValueError
            else:
                old = oldList[idx]
        except:
            print("[Error] 정확한 숫자를 입력하세요.")
            continue
        print(f"\n{str(old)}을 어떻게 수정하시겠습니까?")
        new = input(": ")
        while True:
            print(f"\n{str(old)}를 {new}로 변경하시겠습니까? y/n")
            updateCheck = input(": ")
            if updateCheck == "y":
                old = new
                saveDB(db)
                print("\n[Notice] 할 일이 변경되었습니다. 메인 메뉴로 돌아갑니다.")
                break
            elif updateCheck == "n":
                print("[Notice] 할 일 변경을 취소하고 메인 메뉴로 돌아갑니다.")
                break
            else:
                print("[Notice] y 혹은 n을 입력해주세요.")
                continue
        todoMain(lastId)
        break

""" ----- 할 일 삭제 ----- """
def deleteMenu():
    db = loadDB()  # 프로그램 시작 시 DB 불러오기

    # 메뉴 출력
    print("\n========= [삭제 메뉴] =========")
    print("[1] 전체 삭제\n[2] 날짜 삭제\n[3] 개별 삭제\n[4] 내보내기\n[5] 불러오기")

    # 사용자 선택 입력
    print("어디로 이동할까요?")
    sub = input(": ")

    # 선택에 따른 기능 실행
    if sub == "1":
        deleteAll(db)
    elif sub == "2":
        deleteDate(db)
    elif sub == "3":
        deleteItem(db)
    elif sub == "4":
        saveDB(db)
    elif sub == "5":
        db = loadDB()  # DB 다시 불러오기
    else:
        print("잘못된 입력입니다.")

""" 할 일 관리 """
def manageMenu():
    db = loadDB()

    print("\n========= [관리 메뉴] =========")
    print("[1] 내보내기\n[2] 불러오기")

    print("어디로 이동할까요?")
    sub = input(": ")

    # 선택에 따른 기능 실행
    if sub == "1":
        saveDB(db)
    elif sub == "2":
        db = loadDB()  # DB 다시 불러오기
    else:
        print("잘못된 입력입니다.")


""" ----- 할 일 관리 프로그램 시작 ----- """
newid = ''
newpw = ''
Main(newid, newpw)