# https://school.programmers.co.kr/learn/courses/30/lessons/120809

# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

numbers = [1, 2, 3, 4, 5]

def solution(numbers):
    answer = []
    for i in numbers:
        a = 2*i
        answer.append(a)
    return answer

result = solution(numbers)
print(result)