# https://school.programmers.co.kr/learn/courses/30/lessons/12944

# 문제 설명
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# 제한사항
# arr은 길이 1 이상, 100 이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

arr = [5,5]

def solution(arr):
    answer = 0
    for x in arr:
        answer = answer+x
    average = answer/len(arr)
    return average

print(solution(arr))