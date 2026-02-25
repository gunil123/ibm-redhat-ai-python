# import moduleTest

#sys 모듈: 파이썬에서 제공하는 표준 라이브러리 모듈(실행 관련제어 모듈)
import sys

print(sys) #<module 'sys' (built-in)>
print(sys.path)  #'c:\\python1' 등록되어있음 -> python1폴더에 있는 파일들을 다 imort 할 수 있다

sys.path.append('c:/unit')  #폴더 경로가 등록이 안되어 있음 append로 경로 추가해라.
print(sys.path)
print(type(sys.path))

import moduleTest
print(moduleTest.add(1,2))

