# 파일 입출력
# 읽기: r, 쓰기, w(파일생성), 추가 : a
#파일 읽기
# 절대 경로(C:/test/news.txt), 상대경로("../, ./")
#인코딩 : 문자를 숫자로 바꾸는 것
#디코딩 : 숫자를 문자로 바꾸는 것
#UTF-8 : 가장 많이 쓰는 국제 표준 인코딩(유니코드)
#encoding = 'UTF-5'

f = open('./resource/news.txt', 'r', encoding='UTF-8')
print(f)
print(f.encoding)
print(f.name)
print(f.mode)

#1. read함수 사용
result = f.read()
print(result)
f.close()

#2. 파일객체를 for문과 사용 - 파일을 줄 단위로 읽을 수 있다.
f = open('./resource/news.txt', 'r', encoding='UTF-8')
for line in f:
    print(line)
f.close()

#3. with
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
    c = f.read()
    print(type(c))
    print(list(c))
print("==================================")

with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
    c = f.read(30) #처음 30문자 읽기(UTF-8 기준)
    print(c)
print("==================================")

# 4.readline
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
    line=f.readline() #한 줄씩 출력
    print(line)
    line = f.readline()
    print(line)

print("==================================")

# 5. readlines
with open('./resource/news.txt', 'r', encoding='UTF-8') as f:
    lines=f.readlines() #한 줄씩 출력
    print(lines)
    for i in lines:
        print(i)


#CSV(Comma Seperated Values)
import csv #csv 파일 불러옴

with open('./resource/weather1.csv', 'r') as f:
    reader=csv.reader(f) #파일 객체 f를 읽어 csv 형식에 맞게 줄 단위로 읽겠다.
    print(reader)
    print(type(reader)) #<class '_csv.reader'> 반복가능한 객체(iterable object)

    for i in reader:
        print(i) #리스트 구조로 출력

with open('./resource/weather1.csv', 'r') as f:
    reader = csv.reader(f,delimiter=",") #구분자 쉼표로 설정해서 읽어옴

    for i in reader:
        print(i)
print("===========================================================================")
with open('./resource/weather1.csv', 'r') as f:
    reader = csv.DictReader(f) #csv 파일을 dict로 변환해서 읽어옴

    for i in reader: #한 행을 기준으로(dict)
        for x,y in i.items():  #속성, 데이터값이 반복해서
            print(x,y)   #딕셔너리 구조로 출력됨

print("===========================================================================")


# 쓰기
# w:쓰기(파일 생성)
with open('./resource/test.txt', 'w') as f: #test1.tsx 파일 생성하여 읽음
    f.write('h1 python!!\n') #test1.tsx 파일에 문자열 쓰기
    
with open('./resource/test.txt', 'a') as f: # 문자열 append
    f.write('h1 react!!\n')

# 줄바꿈을 자동으로 추가안함 : writelines         
with open('./resource/test.txt', 'a') as f:
    li=['React\n','DB\n','Python\n']
    f.writelines(li)


