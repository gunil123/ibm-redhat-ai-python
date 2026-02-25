#내장 함수(자주 사용하는 함수 위주)

print(abs(-3))  #3

#all,any : iterable 요소 검사(참, 거짓)
print(all([1,2,3])) #and  True
print(all([1,2,0]))   #False

print(any([1,2,0])) #or(하나라도 참인 요소 있으면 true)

a = [60, 1, 3, 10 , 50]
if all(i > 20 for i in a):  # 리스트 안에 있는 값이 다 20보다 커야 true
    print("ok")
else:
    print("cancle")

a = [60, 1, 4, 10 , 50]
if any(i>30 for i in a):
    print("ok")
else:
    print("cancle") 

#chr : 아스키 -> 문자, ord: 문자 -> 아스키


