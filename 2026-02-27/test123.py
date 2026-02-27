import json

def loading():
    try:
        with open('stu.json', 'r', encoding='utf-8')as f:
            return json.load(f)
        
    except FileExistsError:
        print("파일없음")

def add(data):
    with open('stu.json','w', encoding='utf-8')as f:
        json.dump(data,f, ensure_ascii=False, indent=2)

#print(loading())
datas=[{"name" : "tom", "score" : 100},
{"name" : "Juli","score" : 80}
]
add(datas)
print('저장')