# 함수
# 시작글자 입력해도 함수 안 나오면 ctrl + space
# define 정의
# sum(a,b) -> return
# return 반환
# sum(a,b) => a,b 매개변수
# isPrimary = T/F  => cammel case
# is_primart_key = T/F  => snake case

#Python은 절차 지향(한 줄씩 읽어나가는 것)
#Java는 객체 지향(OP)

def sum(a,b) : 
    return a + b

print(sum(1,2))  #sum(1,2) => 1,2 인수
print(sum(3,5))

def sum1():
    return 2+2
print(sum1())
print()

#argument 매개변수
# *이 붙으면 여러 개 들어갈 수 있는 것
def sum1(*args) : 
    pppp = 0
    for arg in args:
        pppp += arg
    return pppp
print(sum1(1,1,1,1,1,1))  # * : tuple ->리스트니까 * 나오면 for 나오기


def printFunc(**kwargs):
    print(kwargs)
printFunc(a=1, b=1) # ** : dictionary

def makeHuman(name, age) :
    return {"name": name, "age" : age}
human1 = makeHuman("kim", 30)
human2 = makeHuman("park", 34)
print(human1)
print(human2)

def isPrimaryNum(num): 
    isPrimary = True # 소수인가?
    for j in range(2,num) :
        if (num % j == 0):
            isPrimary = False
            break
    if isPrimary :
        return f"{num}은 소수입니다"
    else:
        return f"{num}은 소수가 아닙니다"


def isPrimaryNums(*nums): 
    for num in nums:

        isPrimary = True
        for j in range(2,num) :
            if num % j == 0 :
                isPrimary = False
                break
        if isPrimary :
            print (f"{num}은 소수입니다")
        else:
            print (f"{num}은 소수가 아닙니다")

isPrimaryNums(9,4,2,11,16)

#isPrimaryNums(9,4,2,11,16) -> none
# return 미지정
#print(isPrimaryNums(9,4,2,11,16)) = none


name = "park"  #전역변수; 함수 밖에서 지정된 변수
name1 = "lee"   #전역변수

def setName1(name):  #매개변수
    print(f"2.{name}")
    name1 = name
    name = name  #지역변수
    print(f"3.{name} {name1}")
print(f"1.name1 : {name1}")
print(f"1.{name}")
setName1("kim")  #인자값
print(f"4.{name}")
print(f"2.name1 : {name1}")


#코딩테스트 ; 1.백준(31% 난이도 있음) 2.프로그래머스(30%)