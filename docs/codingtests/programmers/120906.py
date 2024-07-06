# https://school.programmers.co.kr/learn/courses/30/lessons/120906

# 문제 설명
# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요

# 제한사항
# 0 ≤ n ≤ 1,000,000
# 입출력 예
# n	result
# 1234	10
# 930211	16

n = 1234

def solution(n):
    n = str(n)
    answer = 0
    for i in range(len(n)):
        str_ = n[i]
        number = int(str_)
        answer = answer + number
    return answer

print(solution(n))