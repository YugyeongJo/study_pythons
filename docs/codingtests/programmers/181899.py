# https://school.programmers.co.kr/learn/courses/30/lessons/181899

# 문제 설명
# 정수 start_num와 end_num가 주어질 때, start_num에서 end_num까지 1씩 감소하는 수들을 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ end_num ≤ start_num ≤ 50

start_num = 10
end_num = 3

def solution(start_num, end_num):
    answer = []
    for i in range(end_num, start_num+1):
        answer.append(i)
    answer.reverse()
    return answer

print(solution(start_num, end_num))