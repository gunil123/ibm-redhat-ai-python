import threading
import time

def game(name):
    print(f"{name}입장")
    time.sleep(2)
    time.sleep(2)
    print(f"name퇴장")
name = ["정국", "RM","뷔"]

threads = []

for i in name:
    t = threading.Thread(target = game, args=(i,))   # 1.3개 스레드 동시시작
    t.start() #스레드 실행 메소드  #스레드 실행 메소드 #2. 2초동안 기다린 후 3개 스레드가 동시에 종료됨
    threads.append(t)
for t in threads:
    #print(t)
    t.join()  # 모든 작업 스레드 다 끝날때까지 대기

#스레드 객체생성
#Thread: 파이썬 제공 클래스 - > threading 모듈에 정의되었다.
t1 = threading.Thread(target=game, args=("음악",2))
t2 = threading.Thread(target=game, args=("채팅",3))

#스레드 시작메소드 -> target걸었던 함수호출
t1.start()  #game()
t2.start()
print("final")

t1.join() #t1이 끝날때까지 기다림
t2.join() #t2 