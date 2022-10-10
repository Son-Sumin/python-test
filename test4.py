# 1004 복습 - 제어문
a = 5
b = 2
if a > b :
   print(f"{a}는 {b}보다 크다")
elif a < b :
    print(f"{a}는 {b}보다 작다")
else: #위 조건이 다 아니면 마지막으로 실행됨
    print("else")

#1
x = {"company" : "카카오"}
if x.get("company") == "카카오" or x.get("company") == "네이버" :
    print("대기업 직원")
else:
    print("중견기업 직원")

#1-1
x = {"company" : "카카오", "isParttime": True}
if x.get("company") == "카카오" :
    if x.get("isParttime") :
        print("대기업 비정규직원")  
elif x.get("company") == "네이버" :
    if x.get("isParttime") :
        print("대기업 비정규직원")  
else:
    print("중견기업 직원")
#2
# match case 는 or / and 사용불가
match x.get("company") :
    case "카카오" :
        print("대기업 직원")
    case "네이버" :
        print("대기업 직원")
    case _:
        print("중견기업 직원")

#Q. 
phone = {"name" : "갤럭시", "version": "플립"}
if phone.get("name") == "갤럭시" :
    if phone.get("version") == "플립" :
        print("접히네요")
    else :
        print("좋네요")
else:
    print("와우")