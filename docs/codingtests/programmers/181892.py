# https://school.programmers.co.kr/learn/courses/30/lessons/181892

# 문제 설명
# 정수 리스트 num_list와 정수 n이 주어질 때, n 번째 원소부터 마지막 원소까지의 모든 원소를 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 2 ≤ num_list의 길이 ≤ 30
# 1 ≤ num_list의 원소 ≤ 9
# 1 ≤ n ≤ num_list의 길이

num_list = [5, 2, 1, 7, 5]
n = 2

def solution(num_list, n):
    answer = []
    for i in range(n-1, len(num_list)):
        answer.append(num_list[i])
    return answer

print(solution(num_list, n))