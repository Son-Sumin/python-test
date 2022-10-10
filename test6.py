# 2~20까지 짝수의 합
# 방법1
sum = 0
i = 2
while 1 < i < 21 :
    if i%2 == 0 :
        sum += i   
    i+=1
print(sum)

#방법2
i =2
answer = 0
while i <= 20 :
    if i%2 == 0 :
        answer += i
    i+=2
print(answer)

#방법3
answer =0
for index in range(2,21) :
    if index%2 == 0:
        answer +=index
print(answer)

#방법4
# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수 작성
def solution(n:int) :
    answer = 0
    for i in range(1,n+1):
        if i % 2 == 0 :
            answer += i
    return answer

print(solution(10)) 
print(solution(4))   