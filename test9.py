#코딩테스트 ; 1.백준(31% 난이도 있음) 2.프로그래머스(30%)

# 프로그래머스 홀짝 구분하기
# def solution(num):
#     answer = ''
#     if num % 2 == 0 :
#         return "Even"
#     else:
#         return "Odd"
#     return answer


#함수는 return한 순간 끝
# def sum(a,b) :
#     return a+b
# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))


# def sum(a,b) :
#     if a == "짝수": 
#         return
#     print("sum after")
#     for i in range(0,9):
#         print(i)
# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))



# # type 변환
def sum(a,b):
    print(type(a))
    print(type(b))
    try : 
        if type(a) == int and type(b) == int :
            return a+b
        else :
            return int(a) + int(b)
    except:
        return f"{a}랑 {b} 중 숫자가 아닌게 있습니다"

# a = input("입력하세요")
# b = input("입력하세요")
# print(sum(a,b))
# print(sum(2,3))

while True:
    a = input("입력하세요")
    if a =="end":
        break
    b = input("입력하세요")
    if b =="end":
        break
    print(sum(a,b))

for i in range(0, 10):
    a = input("입력하세요")
    if a =="end":
        break
    b = input("입력하세요")
    if b =="end":
        break
    print(sum(a,b))


# 3,6,9 게임
# 3,6,9 대신 c
#계속 지속되어야함
# 369369 현재 {i}


# i = 0
# while True:
#     i += 1
#     myInput = input(f"현재 값 {i}") # "2", "c"
#     answer = str(i+1)
#     for c in str(i+1):
#         # i+1 =13, c=1
#         # i+1 =13, c=3
#         if c=="3" or c=="6" or c=="9":
#             answer = "c"
#         if myInput == answer:
#             print("딩동")
#         else:
#             print("game over")
#             break


# def gama(cur, myInput):
#     answer = str(cur)
#     for c in str(cur):
#         # i+1 =13, c=1
#         # i+1 =13, c=3
#         if c=="3" or c=="6" or c=="9":
#             answer = "c"
#         if myInput == answer:
#             print("딩동")
#             return True
#         else:
#             print("game over")
#             return False

# i = 0
# while True:
#     i += 1
#     myInput = input(f"현재 값 {i}")
#     isWin = gama(i+1, myInput)
#     if(not isWin):
#         break