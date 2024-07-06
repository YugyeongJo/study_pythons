# https://school.programmers.co.kr/learn/courses/30/lessons/181920

# 문제 설명
# 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ start_num ≤ end_num ≤ 50

start_num = 3
end_num = 10

def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num+1):
        answer.append(i)
    return answer

print(solution(start_num, end_num))
