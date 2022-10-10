# for while
from ast import match_case


list = [1,2,3,4,5,6,2,3,5,1]
# for i in list :
#     if i%2 == 0 :
#         print(f"{i} 짝수입니다")
#     elif i%2 == 1:
#         print(f"{i} 홀수입니다")

i = 0
while i < len(list) :
    if list[i]%2 == 0 :
        print(f"list[i] 짝수입니다")
    elif list[i]%2 == 1 :
        # print(f"list[i] 홀수입니다")
        # continue
        # print("끝")
        break
    i+=1


# match case
list1 = [1,2,3,4,5,6,2,3,5,1]
i = 0
for i in list1 :
    match i % 2 :
        case 0:
            print(f"{i} 짝수입니다")
        case 1:
            print(f"{i} 홀수입니다")
i+=1


# 예제) list의 요소를 *2 해서 찍어봐라