# 여러가지 모듈

import calendar
import math
import random
import re
import webbrowser


print("3.141592")
print(math.pi)
calendar.prmonth(2022,10)
# webbrowser.open("https://naver.com")
print(random.random()*11+1)   # random은 0 <= answer <1
   # 0 초과의 결과값을 얻기 위해 +1


#정규식  / 직접 찾아보기
# reg = re.compile("[A-z0-9]{5,15}")
# []: 들어갈 문자들 / {2,5}: 2~5 글자수
reg = re.compile("[0-9]{4,5}") 
id = "22ㅊㅊㅊ42"
id2 = "12345678"
print(reg.match(id))  # match 앞에서부터 조건 완전 일치, 맨 앞은 해당 글자 들어가야함
print(reg.search(id))  # search 조건이 맞는게 있냐?

# 회원가입
# 비밀번호에서 특수문자, 영어, 대문자 포함
# AI 자연어 처리 (ex. 나는 오늘 좋다 는 기분으로 인식)
# 이메일
# reg = re.compile("([A-za-z0-9]+@[A-za-z0-9]+\.[A-za-z]{2,3})")
# print(reg.match("goldkitty007@naver.com"))

#check 필요시 정규식 사용


# 1006 마무리 Quiz
# 로또 1~45 중복없이 6자리
# random, for

# for i in range(0,6) : 
#     num = random.random()*45+1
#     print(int(num))

lotto = []
for i in range(0,5) : 
    numbers = []
    while len(numbers) < 6 : 
        num = int(random.random()*45+1)
        tmpNumber = numbers.copy()
        tmpNumber.append(num)
        setNumbers = set(tmpNumber.copy())
        if len(setNumbers) == len(tmpNumber) :
            numbers.append(num)
    lotto.append(numbers)
for text in lotto:
    print(text)


reg = re.compile("([0-9]{3}-[0-9]{3,4}-[0-9]{4})")
phone_number = '010-2222-9999'
print(reg.match(phone_number))