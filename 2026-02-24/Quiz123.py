
# Q1.
key_input = float(input("키를 실수로 입력하시오")) 
print(f"너의 키는 {key_input}cm이다")
print("너의 키는 {}cm 이다.".format(key_input))

# Q2.
dict1 = dict()
while True:
    name = input("이름을 입력하시오")
    like = input("tv 보는 것을 좋아하는지?")
    dict1[name] = like
    question = input("친구한테도 물어볼까?")
    if(question == "no"):
        break
print(dict1)

# Q3.
def avg(*arg):
    result = 0
    for x in arg:
        result += x
    return result / len(arg)
print(avg(1,2))
print(avg(1,2,3,4,5))

