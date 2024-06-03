# https://school.programmers.co.kr/learn/courses/30/lessons/68935

# 문제 설명
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.

n = 3

def solution(n):
    answer = []

    while True:
        if n < 3:
            answer.append(n)
            break
        rest = n%3
        answer.append(rest)
        n = n//3
        
    result = 0
    for i in range(len(answer)):
        result = result + answer[i]*(3**((len(answer)-1)-i))
        
    return result

print(solution(n))