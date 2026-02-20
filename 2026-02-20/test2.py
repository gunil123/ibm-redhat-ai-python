#리스트 함수
a=[5,3,2,4,1]
a.append(6)
print(a)

a.sort() #오름차순 정렬
print(a)

a.reverse() 
print(a)

print(a.index(5)) #[6, 5, 4, 3, 2, 1] 의 5의 위치

#print(a.insert(2,7)) #인덱스 2에다 7삽입

a.insert(2,7)
print(a)

#리스트를 바꾸는 함수들은 대부분 반환값이 None임

a.reverse() #[6, 5, 7, 4, 3, 2, 1] 거꾸로
print(a)  # [1, 2, 3, 4, 7, 5, 6]

a.remove(1) #[2, 3, 4, 7, 5, 6]
print(a)

a.pop()  
print(a) #[2, 3, 4, 7, 5]

#print(a.pop()) # 6

print(a.pop()) #5 삭제
print(a)  # [2, 3, 4, 7]

print(a.count(4))
print(a.count(1))

ex1=[8,9]
a.extend(ex1)  # [2, 3, 4, 7] + [8,9]
print(a)


li1=[]
li2=list()
li3=[4,2,6,7,1]
li4=[3,3,'jack','tom']
li5=[1,3,['banana','apple','orange']]
li6=[2,True, False, 'mango','coffee',3.43]
#li4 의 tom출력
print(li4[3])

#li5 의 apple출력
print(li5[2][1])

#li4거꾸로 출력
# li4.reverse()
# print(li4)
print("========")
print(li4[::-1])

a="abcdefg"
print(a[0:5:2])