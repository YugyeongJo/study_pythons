# https://school.programmers.co.kr/learn/courses/30/lessons/181896

# 문제 설명
# 정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.

# 제한사항
# 5 ≤ num_list의 길이 ≤ 100
# -10 ≤ num_list의 원소 ≤ 100

num_list = [12, 4, 15, 46, 38, -2, 15]

def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            break
        else:
            answer = -1
    return answer

print(solution(num_list))