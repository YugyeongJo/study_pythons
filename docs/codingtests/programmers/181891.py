# https://school.programmers.co.kr/learn/courses/30/lessons/181891

# 문제 설명
# 정수 리스트 num_list와 정수 n이 주어질 때, num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 2 ≤ num_list의 길이 ≤ 30
# 1 ≤ num_list의 원소 ≤ 9
# 1 ≤ n ≤ num_list의 길이
# 입출력 예
# num_list	n	result
# [2, 1, 6]	1	[1, 6, 2]
# [5, 2, 1, 7, 5]	3	[7, 5, 5, 2, 1]

num_list = [2, 1, 6]	
n = 1

def solution(num_list, n):
    answer01 = []
    answer02 = []
    for i in range(len(num_list)):
        if i < n:
            answer01.append(num_list[i])
        else:
            answer02.append(num_list[i])
    answer = answer02+answer01
    return answer

print(solution(num_list, n))