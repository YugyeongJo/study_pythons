# https://school.programmers.co.kr/learn/courses/30/lessons/120824

# 정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

num_list = [1, 3, 5, 7]

def solution(num_list):
    answer = []
    num1 = 0
    num2 = 0
    for i in num_list:
        if i%2 == 0:
            num1 += 1
        else:
            num2 += 1
    answer = [num1, num2]
    return answer

result = solution(num_list)
print(result)