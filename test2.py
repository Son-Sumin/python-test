# 제어문
a = 10
b = 5
# print(f "a > b {a>b} = True 크다 False 작다")
# : 뒤에는 tab으로 무조건 띄어쓰기
str1 = ""
if a>b : 
    # 조건이 True면 아래 문장을 실행한다
    str1 = "크다"
    print(f"a>b 크다")
elif a<b : 
    # elif 위의 조건이 아니면(False) 이걸 실행
    str1 = "작다"
    print(f"a<b 작다")
else : 
    # if False, elif False 다 아니면 실행
    str1 = "같다"
    print(f"a>b {str1} ")

c = [1,2,3]
if len(c) > 3 :
    print(c[0])
if len(c) > 2 :
    print(c[1])


# 반복문
a = ["a", "b", "c", "d", "e"]
# 0 <= i < len(a)=5
for i in range(0, len(a)) :
    print(i)
    print (a[i])
# step은 미기재시 기본 1
for i in range(0, 5, 2) :
    print(i)
    print (a[i])
#foreach
for i in a :  # 여기서 i는 a의 원소
    print(i)

re = 0
while re < 5 :
    print(a[re])
    re+=1 # re = re(0) + 1 = 1
    
b = [1,2,3,4,5]
re = 0
while True :
    print(b[re])
    if(b[re] % 2 ==0) :
        break # 반복 중지 (=ctrl C)
    re+=1
for i in a :
    if i =="c" :
        break
    print(i)