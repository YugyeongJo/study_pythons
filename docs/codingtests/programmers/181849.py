# https://school.programmers.co.kr/learn/courses/30/lessons/181849

# 문제 설명
# 한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ num_str ≤ 100
# 입출력 예
# num_str	result
# "123456789"	45
# "1000000"	1

num_str = '123456789'

def solution(num_str):
    answer = 0
    for num in num_str:
        answer += int(num)
    return answer

print(solution(num_str))