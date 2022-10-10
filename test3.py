#list = [1,2,3,4,5,6,2,3,5,1]
#뭐는 짝수입니다.
#뭐는 홀수입니다.

from functools import reduce


list = [1,2,3,4,5,6,2,3,5,1]

for i in list :
    if i % 2 == 0:
        print(f"{i}은 짝수입니다")
    elif i % 2 == 1:
        print(f"{i}은 홀수입니다")

i = 0
while i < len(list) :
    if list[i] % 2 == 0:
        print(f"{list[i]}은 짝수입니다")
    elif list[i] % 2 == 1:
         # print(i)
        # print(f"{list[i]}은 홀수입니다")
        # continue #반복문의 continue 뒤 실행 X, break 반복문 끝남
        break
        # print("끝")
        i +=1


    # match, case
    # java switch case
    list1 = [1,2,3,4,5,6,2,3,5,1]
    for el in list1 :
        match el % 2 :
            case 1:
                print(f"{el}은 홀수입니다")
            case 0:
                print(f"{el}은 짝수입니다")


    # 람다 버전3.6부터
    # 예제) list의 요소를 *2 해서 찍어봐라
    list1 = [1,2,3,4,5,6,2,3,5,1]
    list2 = []
    for el in list1:
        list2.append(el*2)
    print(list2)

    list3 =[]
    for el in range(0, len(list1)) :
        list3.append(list1[el]*2)
    print(list3)

# map은 새로운 리스트를 만든다(반환한다)
    list4 = list(map(lambda el: el**2, list1))
    print(list4)


# tmpd = {"name" : "re", "age" : 100}
# list5 = [tmpd, tmpd, tmpd]
# list6 = list(map(lambda el: el.copy(), list5))
# #[tmpd.copy(), tmpd.copy(), tmpd.copy()]
# list7 = list5.copy() #[tmpd, tmpd, tmpd]
# print(list5)
# print(list6)
# print(list7)
# list5.append(1)
# print()
# print(list5)
# print(list6)
# print(list7)
# tmpd["age"] = 10
# print()
# print(list5)
# print(list6)
# print(list7)

# list1 요소의 합? int(수)
list1 = [1,2,3,4,5,6,2,3,5,1]
sum = 0
for el in list1:
    sum = sum + el
    #sum += el
print(sum)

sum2 = reduce(lambda x,y: x+y, list1)
# 합계 구할때 사용함
print(sum2)

#----------------------------
list1 = [1,2,3,4,5,6,2,3,5,1]
#4이상으로만(조건) 리스트 만들기
list0 = []  #리스트를 만들기 위해 리스트를 선언함
for el in list1 :
    # print(el)
    if el >= 4 :
        list0.append(el)
print(list0)

list2 = list(filter(lambda x: x >= 4, list1))
print(list2)