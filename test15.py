# 1. 자연수 뒤집어 배열로 만들기
# 2. 제일 작은 수 제거하기
# 3. 두 정수 사이의 합
# 4. 정수 제곱근 판별


# 3. 두 정수 사이의 합
def solution(a, b):
    answer = 0
    if a<b :
        # list1 = list(range(a,b+1))
        # answer = sum(list1)
        return sum(range(a,b+1))
    elif a>b :
        list1 = list(range(b,a+1))
        answer = sum(list1)
    else :
        answer = a
    return answer
print(solution(3,5))
print(solution(3,3))
print(solution(5,3))




# list1 = [1,2,3,4,5,6,2,3,5,1]
# sum = 0
# for el in list1:
#     sum = sum + el
#     #sum += el
# print(sum)

# sum2 = reduce(lambda x,y: x+y, list1)
# # 합계 구할때 사용함
# print(sum2)


# list1 = [a,b]
# def solution(a, b):
#     set = {a,b}
#     print(set{0})
#     answer = 0
#     for i in range(int(set{0}),int(set{1})):
#         answer += i    
#     return answer
# print(solution(3,5))
# print(solution(3,3))
# print(solution(5,3))


# # 2. 제일 작은 수 제거하기
# def solution(arr):
#     answer = []
#     if len(arr)==1 :
#         return [-1]
#     minNumber = 1000000
#     for a in arr : 
#         if a < minNumber : 
#             minNumber = a
#     arr.remove(minNumber)
#     return arr
#        # for a in arr :
#        #     if minNumber != a :
#        #         answer.append(a)
#        # return answer
# print(solution([10]))
# print(solution([4,3,2,1]))




# 1. 자연수 뒤집어 배열로 만들기

# a = 123 #백이십삼
# a[0] is error
# b = "123" #일이삼
# b[0] = "1"
# answer = []
# arr = list(str(a)) #문자로 변경한 이유는 하나씩 뜯어 놓으려고
# arr.reverse()
# print(arr)  #['3','2','1']

# for i in range(0,len(arr)) :
#     answer.append(int(arr[i]))
# print(answer)


def solution(n):
    answer = []
    strA = str(a)
    for i in range(len(strA)-1,0,-1):
        answer.append(int(str[i-1]))
    return answer

# n = 12345
# answer = list(str(n))
# print(answer)
# answer.reverse()
# print(answer)
# for x in answer :
#     return answer



# def solution(n):
#     answer = []
#     return answer

# 4. 정수 제곱근 판별
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if i * i == n :
            answer = (i+1)*(i+1)
            break
        elif i * i > n:
            break
    if answer == 0 :
        return -1
    return answer
print(solution(121))
print(solution(3))
print(solution(1))