# 정적; 변화가 없다
from typing import overload


class Calc:
    @staticmethod  # @는 어노테이션이라 칭함 / self -> 변수 가 됨
    #선언을 하면 self가 생김
    def add(a,b):
        print(a+b)

    @staticmethod
    @overload  # 생긴 것은 똑같은데 쓰임이 다를 경우 활용
    def diff(s,a,b):
        print("diff 3개짜리")

    @staticmethod
    @overload
    def diff(s,a):
        print("diff 2개짜리")

    
    # python은 절차지향이기에 위의 상황인 경우
    # 두 번째 diff로 쓰이게 됨