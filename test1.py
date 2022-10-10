print('Q1. ')
a = [12,21,1,2,3,4,5,89,65,15,74]
setA = set(a)
list[setA]
a.reverse()
print(a)
a.sort()
print(a)



print('Q2. ')
a = {"name" : "park", "score" : 70}
b = {"name" : "kim", "score" : 80}
c = {"name" : "park", "score" : 50}
print("%s는 점수가 80점 이상이 %s\n" %(a.get("name"), a.get("score")>=80))
print("%s는 점수가 80점 이상이 %s\n" %(b.get("name"), b.get("score")>=80))
print("%s는 점수가 80점 이상이 %s\n" %(c.get("name"), c.get("score")>=80))

print("%s는 점수가 80점 이상이 %d\n" %(a.get("name"), a.get("score")>=80))
print("%s는 점수가 80점 이상이 %d\n" %(b.get("name"), b.get("score")>=80))
print("%s는 점수가 80점 이상이 %d\n" %(c.get("name"), c.get("score")>=80))



print('Q3. ')
p1 = {"name" : "kim", "money" : 50000}
p2 = {"name" : "park", "money" : 30000}
print("%s는 %s보다 %d 있습니다." %(
p1.get("name"), p2.get("name"), 
p2.get("money")-p1.get("money")))


p1 = {"name" : "kim", "money" : 50000}
p2 = {"name" : "park", "money" : 30000}
print("%s과 %s의 합 %.d 있습니다." %(
p1.get("name"), p2.get("name"), 
p1.get("money")+p2.get("money")))


p1 = {"name" : "kim", "money" : 50000}
p2 = {"name" : "park", 'money' : 30000}
print("%s와 %s의 평균은 %.0f입니다." %(
p1.get("name"), p2.get("name"),
(p1.get("money")+p2.get("money"))/2))



print("복습문제1")
a = {"num" : 80}
print("%s는 %d이다" %(a.get("num"), (a.get("num")%2 == 0)))
print(f"80은 짝수인가 {80%2 == 0}")



print("복습문제2")
list1 = [2,1,5,6,2,40,50,2,5,32]
list2 = [4,6,2,3,9,10,2,3,42,5,4,63]

print(list(set(list1) & set(list2)))  # set: 중복제거 후 최소부터 나열 /  &: 교집합
print(set(list1))
print(set(list2))
union = list(set(list1) & set(list2))
print(union)
union.sort()  # 정렬
print(union)
print(union[len(union)-1])  # union 집합에서 맨 마지막 요소 출력

# tmpd = {"name" : "re", "age" : 100}
# list = [tmpd]
# list1 = list
# list2 = list.copy()
# list3 = [tmpd.copy]
# print("list")
# print(list)
# print("list1")
# print(list1)
# print("list2")
# print(list2)
# print("list3")
# print(list3)

# list.append(1)
# print("list")
# print(list)
# print("list1")
# print(list1)
# print("list2")
# print(list2)
# print("list3")
# print(list3)

# tmpd["name"] = "lee"
# print("list")
# print(list)
# print("list1")
# print(list1)
# print("list2")
# print(list2)
# print("list3")
# print(list3)

# print("----------------------------------------")
# print(list1)
# list1.sort()
# print(list1)

# # print("----------------------------------------")
# testBool1 = True
# testBool2 = False
# testBool3 = 3 >0

# dict1 = {"name" : "park", "age" : 30}
# dict1.get("name")