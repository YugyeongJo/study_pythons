# https://school.programmers.co.kr/learn/courses/30/lessons/120583

# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

array = [0, 2, 3, 4]	
n = 1

# def solution(array, n):
#     answer = 0
#     for i in range(len(array)):
#         if array[i] == n:
#             answer += 1
#     return answer

def solution(array, n):
    answer = array.count(n)
    return answer

result = solution(array, n)
print(result)