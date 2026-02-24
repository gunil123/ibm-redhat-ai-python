# Q1
국어 = 80
영어 = 75
수학 = 55
print((국어+영어+수학)/3)

#Q2
n = 13
if n % 2 == 0:
    print('짝수')
else:
    print('홀수')

#Q3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:14]
print('19'+yyyymmdd)
print(num)

#Q4
pin = "881120-1068234"
print(pin[7])

#Q5
a = "a:b:c:d"
b = a.replace(':',"#")
print(b)

#Q6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

#Q7
a = ['Life', 'is', 'too', 'short']
result = ",".join(a)
print(a)

#Q8
a = (1, 2, 3)
a = a + (4,)
print(a)

#Q9
a = dict()
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python'
a[250]= 'python' # a[[1]] = 'python' TypeError: unhashable type: 'list'
#딕셔너리의 키로 변하는 값을 사용할 수없기 때문이다. 키값에 리스트 쓸 수 없다.
print(a)

#10
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B') #result = a.get('B')
print(a)
print(result)

#11
a = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)

#12
a = b = [1,2,3]
a[1] = 4
print(b) #[1, 4, 3]  b값은 2가 4로 바뀌고, a와 b 모두 동일한 리스트를 가지기 때문이다.