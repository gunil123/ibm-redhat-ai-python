#파이썬은 패키지로 분할된 개별적인 모듈로 구성
#상대경로: ..(부모 디렉토리) .(현재 디렉토리) 

#1)import 패키지명.하위패키지.모듈명
import pro_test.test1.module1
import pro_test.test2.module2

pro_test.test1.module1.mod1_test1()
pro_test.test1.module1.mod1_test2()

pro_test.test2.module2.mod2_test1()
pro_test.test2.module2.mod2_test2()

print("=========================================")
#2)from 패키지명.하위패키지 import 모듈명
from pro_test.test1 import module1
from pro_test.test2 import module2 as m2 #Alias

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print("=========================================")
#p.215
#3)from 패키지명 import *
from pro_test.test1 import *
from pro_test.test2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()

