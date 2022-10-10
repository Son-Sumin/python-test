#반복문
# while : 조건이 True인 동안 아래를 실행함
# for i in list1, range(0,3)
# i = index
for i in range(0, 3) :
    print(i)

list1 = ["a", "b", "c"]
for i in range(0, len(list1)):
    print(list[i])

for element in list1 :
    print(element)

index = 0
while index  < len(list1) :
    print(list1[index])
    index+=1

# break continue
# list1 = [9,4,2,1,6,7,5,4,3,7]
# 만약에 홀수면 2배, 짝수면 그냥의 리스트를 만드는 중
# 합이 20이 넘으면 끝

list1 = [9,4,2,1,6,7,5,4,3,7]
list0 = []
i = 0
sum1 = 0
while i < len(list1) :
    sum1 += list1[i]
    # sum1 = sum1 + list1[i]
    if list1[i]%2 == 1 : 
        list0.append(list1[i]*2)
    else:
        list0.append(list1[i])
    i+=1
    if sum1 > 20 : 
        break
    #     continue
    # print("끝")
print(list0)


list1 = ["안", "녕", "하", "세", "요"]
index = 0
hi = ""
while index < len(list1) : 
    print(hi)
    hi += list1[index]
    print(hi) #출력값
    index+=1
print(hi) #출력값


for i in range(0,len(list1),2) :
    hi += list1[i]
print(hi)


for element in list1 :
    hi = hi + element
print(hi)


# num =5
# for element in num :
#     print(element)

st = "안녕하세요"
print(st[0])
for element in st:
    print(element)