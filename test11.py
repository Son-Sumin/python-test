# 계산기 만들기
# 기본적으로

# def add(a, b):
#     return a+b

# def diff(a,b):
#     return a-b

# i = 0
# i = add(i, 10)
# i = diff(i,5)
# print(i)

# j = 0
# j = add(j, 10)
# j = diff(j,5)
# print(j)

#class : 함수들의 모음 (init: 초기값 설정, self: 자기자신)
# class Calculator:
#     def __init__(self) -> None:
#         self.result = 0

#     def add(self, b):
#         self.result += b
        
#     @overload
#     def add(self, b, c):
#         self.result = self.result + b + c

#     def diff(self,b):
#         self.result -= b

#모듈
from animal import Animal
from cat import Cat
from dog import Dog
from human import Human
from test12 import Calculator
from user import User
from leg import Leg
from arm import Arm


a = list()
a.append("1")
b = list()
b.append("2")
print(a)
print(b)

cal1 = Calculator()   #ctrl + space
cal1.add(10)
cal1.diff(5)
print(f"cal1\t{cal1.result}")

cal2 = Calculator()
cal2.add(10)
cal2.diff(5)
print(f"cal2\t{cal2.result}")


# @overload : 같은 이름인데 다른 기능으로 쓰이는 것


def arer(a,b):
    return a+b

user1 = User("bit", "1234")
user1.printUser()
user1.change_id("pppp")
user1.printUser()

l= Leg("left", "son")
# a= Arm("left", "son")
print(l.side)
print(l.name)
l.setName("kim")
print(l.name)


an = Animal()
print(an.name)
an.__setattr__("name", "?")
print(an.name)
print(an.__dict__)
#__ 이후 나오는 보라색은 함수, 파란색은 변수

cat = Cat()
cat.printSound()
print(cat.name)
print(cat.butler)

dog = Dog()
dog.printSound()
print(dog.name)
print(dog.master)
print(dog.__dict__)

# class ; 객체 지향  ->  Java 때 더 자세히 배울 예정
# cf. 절차지향
# human = {"name": "park", "age : 46, gender: "남"}

# class는 상위버전 갖고와서 사용 가능
# class는 하나의 물체를 만들기 위해 사용
# 상속, 즉 공통 코드를 줄이기 위해 class 사용