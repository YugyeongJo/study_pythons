# https://school.programmers.co.kr/learn/courses/30/lessons/181935

# 문제 설명
# 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ n ≤ 100
# 입출력 예
# n	result
# 7	16
# 10	220

n = 10

def solution(n):
    answer = 0
    if n % 2 != 0:
        for x in range(n+1):
            if x % 2 != 0:
                answer += x
            else:
                pass
    if n % 2 == 0:
        for x in range(n+1):
            if x % 2 ==0:
                answer += x**2
            else: 
                pass
    
    return answer

print(solution(n))