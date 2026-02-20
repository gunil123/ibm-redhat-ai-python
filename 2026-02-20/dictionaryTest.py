#딕셔너리
#순서 x, 키 중복 x, 수정 O,  삭제 O
dic1 = {'name':'Lee', 'phone':'010-1234-1234', 'borth':'00021'}
dic2= {0:'python'}
dic3={'ary':[1,2,3,4]}
dic4={
    'name':'tom',
    'addr':'seoul',
    'age' : '22',
    'grade':'A',
    'status':True
}
dic5=dict() 
print(dic5)
dic6=dict([('name','tom'), ('addr','seoul'), ('age' , '22'), ('grade','A'),('status',True)])

# 가장 안쪽 구조 : 튜플 구조
# 안쪽을 감싸는 구조 : 리스트 구조(여러 개의 튜플을 하나로 묶음 -> 튜플의 리스트)
# 가장 바깥쪽 구조 : 딕셔너리 구조로 변환해줘

#(키, 값 )튜플 -> 튜플들의 리스트 -> dict() - > 딕셔너리{키:값}
print(dic1)
print(dic6)
#dict()함수는 인자를 1개만 받는 구조!!

# p.96
#key를 이용해 value값 추출
#딕서너리명['키명']
#print(dic1['name1']) #키 값이 있으면 출력, 없으면 keyError
print(dic1.get('name'))

print(dic2[0])
print(dic2.get(0))

# 기존 값 덮어씀(키값 중복되면)
a={1:'c', 1: 'a', 1:'b', 1: 'd'}
print(a)

dic1['address']='yougsan'
print(dic1)
#딕셔너리 함수들
print(dic1.keys()) #키들의 집합
print(dic2.keys())

print(list(dic1.keys())) #리스트형으로 변환해서 출력
print(list(dic3.keys()))

print(dic1.values()) #값(value)들의 집합
print(list(dic1.values())) #리스트형으로 변환해서 출력

print(dic3.items()) #키, 값 쌍 다 출력
print(list(dic3.items()))

print(dic1.pop('name')) #키 값 넣어서  삭제 -> 값도 같이 삭제됨
print(dic1)

#dic1에 'name' 키 속성이 있는지 확인(in)
#p.101
print('name' in dic1)