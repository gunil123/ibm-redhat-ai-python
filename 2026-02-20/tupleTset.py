tu1 = ()
tu2 = (1,)
tu3 = (1, 2, 3, 4)
tu4 = (2, 3, 'apple', 'banana')
tu5 = (2, 3 , ('apple', 'banana', 'mango'))

print(type(tu4))
print(tu4[1])
print(tu4[0] + tu4[1])
print(tu5[-1][1])

# tu4[0] = 20 #값 수정 불가능
# print(tu4)

#del tu4[0] #값 삭제 불가능

print (tu4[2:])

#튜플연산
print(tu3+tu4)
print(tu3*4)
print(str(tu3[0])+"hello")

tu=(5,2,4,4,3)
#5의 위치
print(tu.index(5))
#4의 개수
print(tu.count(4))

# 팩킹(packing) : 여러 값을 하나의 튜플, 딕셔너리, 리스트 등으로 묶는 것
# 언팩킹(unpacking) : 튜플, 딕셔너리, 리스트 등으로 묶여 있는 값을 개별(각각) 변수로 푸는 것

x = 2
y = 3
z = 4

pack1 = (x, y, z) #packing
pack2 = [x, y, z] #packing
print(pack1)

(x,y,z) = pack1 #unpacking
print(x, y, z) 


tu33 = 1,2,3 #튜플 팩킹
tu44 = 4,

#tu33언팩킹
x1,x2,x3=tu33
x4, x5, x6 = 4, 5, 6 #튜플 언팩킹이고, ()소괄호 생략됨
print(x4, x5, x6)

