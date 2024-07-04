# https://school.programmers.co.kr/learn/courses/30/lessons/120862

# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# -10,000 ≤ numbers의 원소 ≤ 10,000
# 2 ≤ numbers 의 길이 ≤ 100
# 입출력 예
# numbers	result
# [1, 2, -3, 4, -5]	15
# [0, -31, 24, 10, 1, 9]	240
# [10, 20, 30, 5, 5, 20, 5]	600

# 1) list 내 값들을 정렬하기
# 2) 음수 기준 맨 왼쪽 2개의 값 또는 양수 기준 맨 오른쪽 2개의 값을 각각의 변수에 저장
# 3) if문을 사용하여 더 큰 값을 새로운 변수에 저장 후 출력

numbers = [1, 2, -3, 4, -5]

# 방법1)
# def solution(numbers):
    
#     numbers.sort(reverse=True)
#     minus_mul = numbers[0]*numbers[1]
#     plus_mul = numbers[-1]*numbers[-2]
    
#     if minus_mul > plus_mul:
#         answer = minus_mul
#     else:
#         answer = plus_mul        

#     return answer

# 방법 2)
def solution(numbers):
    numbers.sort(reverse=True)
    answer = max(numbers[0]*numbers[1], numbers[-1]*numbers[-2])
    
    return answer


print(solution(numbers))

