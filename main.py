#main / 항상 최상위 폴더에 생성할 것
#main 내가 실행시킬 것
#java는 무조건 main start

#다른 폴더에 있는 class 사용 시 class 있는 파일에__init__ 파일 만들기

#package
# from calculator.add import add
# # from calculator.diff import diff
# # from aatest.input import testInput
# from aperson import APerson
# # from user.age import showAge
# # from user.name import showName

# # test4()


# def main() :
# #     # count = 0 
# #     # count = add(count,4)  # 4
# #     # count = diff(count,10) # -6
# #     # print(count)  # -6
# #     # text = testInput()
# #     # print(text)

# #     # showName("son")
# #     # showAge(21)

# #     a = APerson()
# #     b = APerson()
#     c = APerson()
# #     print(a.count)
# #     print(b.count)
#     print(c.count)
#     c.printCount()
#     c.printCount2()



# # from calc import Calc

# # Calc.add(1,3)
# # Calc.diff(1,3)

# main()
# class animal():
#     def __init__(self) -> None:
#         print("동물")
#         pass
# animal()


#프로그래머스 피보나치수열  
# n은 무조건 int가 들어올 수 있게끔 타입 부여함

# def solution(n:int) : 
#     answer = 1
#     first = 0
#     second = 1
#      # answer = first + second
#     for i in range(2, n+1):
#         answer = first + second
#         first = second
#         second = answer
#     return answer % 1234567

# print(solution(3))
# print(solution(5)) 

def arrAppend(arr: list):  # arr : list 에서 :는 타입 부여
    arr.append()