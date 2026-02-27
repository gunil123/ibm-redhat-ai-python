#chr : 아스키 -> 문자, ord: 문자 -> 아스키
print(chr(65))
print(ord('A'))

#enumerate : 인덱스 + iterable 객체
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# filter : 반복가능한 객체 요소를 지정한 후 조건에 맞는 값 추출
def num(x):
    return abs(x) > 3
print(list(filter(num, [-3,2,4,-4,-10,-100])))

# lambda로 바꾸기
print(list(filter(lambda x : abs(x)>3, [-3, 2, 4, -4, -10, -100])))

# id : 객체의 주소값 반환
print(id(int(10)))
print(id(10))
print(id(11))

#len : 길이반환
print(len('python'))
print(len([1,2,3,4,5]))

#p.250
#map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
# 반복가능한 객체 : 리스트, 튜플, 문자열

def num2(x):
    return x
#map(함수명넣어서)
#map(lambda)
print(list(map(num2, [1,2,3,4,5])))

print(list(map(lambda x:x, [1,2,3,4,5,6])))

#range: 반복가능한 객체 반환
print(range(5))
print(range(1,10,2))
print(list(range(1,10,2)))
print(list(range(0,10,-1)))

for i in range(5):
    print(i)

#p. 251
# max, min 최대, 최소
print(max([100,223,34242]))
print(min(1,2,3))

#round : 반올림
print(round(4,6))
print(round(3.12421414,2))

#sorted: 반복가능한 객체 정렬 후 반환
print(sorted([5,6,2,1,3,4,3,3,4]))
a = sorted([4,5,6,2,1,2,4,2])
print(a)
print(sorted(['p', 'y', 'y', 'h', 'o', 'n']))

#sum : 반복가능한 객체 합 반환
print(sum([1,2,3,45]))

#type : 자료형 확인
print(type(3))
print(type({}))
print(type(()))
print(type([]))

#p.225
#zip: 반복가능한 객체의 요소 묶어서 반환(인덱스 순서대로 묶임)
print(list(zip([10,20,30], [40,50,60])))