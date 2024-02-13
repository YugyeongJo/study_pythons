# https://school.programmers.co.kr/learn/courses/30/lessons/120831

# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

n = 4
 
def solution(n):
    answer = 0
    for i in range(n):
        if 2*i <= n:
            answer = answer+(2*i)
        else :
            answer = answer
    return answer

result = solution(n)
print(result)