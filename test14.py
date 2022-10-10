# MySQL, NoSQL, 자바
# hadoop
# 웹프론트, 백엔드 (javascript,java)
# 머신러닝 딥러닝 텐서플로 (python)
# MySQL, NoSQL, DB

# 파이썬은 절차지향 언어이다
# type
# int(숫자), str(문자), list, set, tuple, dict 
# int 선언 : a=1
# str 선언 : "stt"
# list 선언 a=[]
# set 선언 a={}
# tuple 선언 a=()
# dict 선언 a={key:value}
# 이와 같은 것을 동적 타이핑이라 칭함
# 장점 : 타입 지정하지 않아도 사용 가능
# 단점 : 오류 발생 가능

# 스크립트 언어
# 소스코드를 한 줄씩 읽어 곧바로 실행
# python 문법으로 코드를 작성했는데 컴퓨터 언어는 이진법으로 표현함
# 컴파일 python - > 컴퓨터 언어로 표현
# 따로 컴퓨터 언어(기계언어)로 바꿔서 따로 파일을 만들어 그것을 시행하지 않아도 됨
# 장점; 플랫폼 독립적 : os 상관없음(window, linux...)

# 제어문
# if elif else
# match case

# 반복문
# for in :
# while (whileTrue)
# break continue
# lambda(map, reduce, filter)

from functools import reduce


list1 = [9,1,2,4,3]
def sum(x,y):
    print(f"{x} {y}")  #format
    return x+y
a = reduce(lambda x,y: sum(x,y), list1)
print(a)
string = reduce(lambda x,y: sum(x,y), "abcde")
print(string)
# reduce 결과값을 누적해서 연산

user = {"id":"id", "pass":"pass", "name":""}
names = ["kim", "lee", "park"]
namelist = list(map(lambda x : {"id":"id", "pass":"pass", "name":x, "age":30}, names))
print(namelist)
# map 리스트 항복마다 함수를 적용해주는 고차함수

numlist = input().split()
result = list(map(int, numlist))
#numlist의 항목을 int로 바꾸는 코드
#input()으로 입력받은 항목은 모두 str 취급

findUser = list(filter(lambda x : x.get("name")=="park", namelist))
print(findUser)
#filter 합수부분에 조건 넣기, 그 조건에 맞으면 반환

avgAge = reduce(lambda x,y: x+y.get("age"), namelist,0)
print(avgAge/len(namelist))

# 함수
# def
# def sum(a,b):  a,b: 매개변수
#     return a+b
# sum(1,2)   1,2: 인수

# def sum(*a) : *a tuple
# sum(1,2,3,4)
# def sum(**a) : **a dict
# sum(name=kim, age=56)

# name = "kim" 전역변수
# def printName(name):
# name = "lee"  지역변수

# 파일 입출력
# f = open(파일, mode,)
# encoding UTF-8 ; 한글 사용할 때 사용

# 입력받고 싶을 때 : input

# class
# 사용 이유; 중복되는 것을 한 번에 처리하기 위해
# 객체지향
# class name(상속):
#   def__init__:
# 상속 접근할 때 super()
# def__init__(self):  *self: 자신

# import ; 다른 곳에서 파일 불러올 떄 사용

# 정규식 개념 search match 
#  ex. goldkitty007@naver.com 이 이메일 형식이 맞는지?
# import re

# import random

# from datetime import date
# print(date.today())


# C:\test (현위치) -> C:\test\test2
# 상대경로
# ./test2 라고 입력
# ../ ; 상위폴더로 가기

# 절대경로
# C:\test\test2

# 논코드
# 머신러닝; 자동코드 추천(시작점)