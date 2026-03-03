import pickle
import os

TODO_DB_PATH = "test.obj"

def exportDB(db):
    try:
        with open(TODO_DB_PATH, "wb") as f:
            pickle.dump(db, f)
        print("\n[성공] 파일 저장이 완료되었습니다. (내보내기)")
    except Exception as e:
        print(f"\n[오류] 저장 중 문제가 발생했습니다: {e}")

def importDB():
    if not os.path.exists(TODO_DB_PATH):
        print("\n[알림] 저장된 파일이 없습니다. 빈 데이터를 반환합니다.")
        return {}
    
    try:
        with open(TODO_DB_PATH, "rb") as f:
            loaded_db = pickle.load(f)
            print("\n[성공] 파일 불러오기가 완료되었습니다. (불러오기)")
            return loaded_db
    except (EOFError, FileNotFoundError):
        return {}

def viewAll(db):
    if not db:
        print("\n[알림] 등록된 할 일이 없습니다.")
        return

    print("\n========= [전체 할 일 목록] =========")
    for date in sorted(db.keys()):
        tasks = ", ".join(db[date])
        print(f"▶ 날짜: {date} | 할 일: {tasks}")
    print("=====================================")

def viewByDate(db):
    if len(db) == 0:
        print("등록된 데이터가 없습니다.")
        return

    target = input("조회할 날짜를 입력하세요 (예: 2_27): ")

    if target in db:
        print(f"--- {target} 할 일 목록 ---")

        tasks = db[target]
        for task in tasks:
            print("-", task)
    else:
        print("해당 날짜에 등록된 할 일이 없습니다.")

def viewMenu(db):
    print("\n1. 전체 보기 / 2. 날짜별 보기")
    choice = input("선택: ")
    
    if choice == "1":
        viewAll(db)
    elif choice == "2":
        viewByDate(db)
    else:
        print("\n[알림] 잘못된 입력입니다.")