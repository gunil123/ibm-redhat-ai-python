# 문제1. odd=[1,3,5,7,9]에서 1,3 각각 출력후 10을 1이 있는 자리 대입
odd=[1,3,5,7,9]
print(odd[0])
print(odd[1])
odd[0]=10
print(odd)

# 문제 2. 
a=[1,2,3,4,5]
b=[6,7,8,9,10]

print(a+b)
a.append(6)
print(a)

a.insert(3, 7)
print(a)

a.pop()
print(a)

del a[3]
print(a)

a.remove(4)
print(a)

print(a.index(5))
