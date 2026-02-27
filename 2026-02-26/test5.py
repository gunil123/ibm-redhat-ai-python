#sys, pickle, os, time, random 등

#sys : 실행 관련 제어
import sys
# print(sys.argv)


print("start")
# sys.exit() #프로그램 즉시 종료
print('end')

# 파이썬 패키지 위치
print(sys.path)

#p.273
# ** pickle : 객체 파일 쓰기 **
import pickle
f = open('test.obj', 'wb')  #파일을 쓰기용 바이너리 모드로 열기
obj = {1:'python', 2:'study', 3:'basic'}
pickle.dump(obj,f)  #객체를 파일에 저장(직렬화)
f.close() 

import pickle

with open('test.obj', 'wb') as f:
    pickle.dump(obj, f)

import os
print(os.environ)
print(os.getcwd()) #현재경로

import time
# 현재 시간 리턴
print(time.ctime())

# 포맷코드(형식표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


#random : 난수리턴
import random
print(random.random()) #0.0이상 ~1.0 미만의 실수

print(random.randint(1,45)) #1~45 포함 정수

# 섞기
d = [1,2,3,4,5]
random.shuffle(d)

# #p.286
# import webbrowser
# webbrowser.open('http://www.google.com')
