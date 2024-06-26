# https://school.programmers.co.kr/learn/courses/30/lessons/181928

# 문제 설명
# 정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와 짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 2 ≤ num_list의 길이 ≤ 10
# 1 ≤ num_list의 원소 ≤ 9
# num_list에는 적어도 한 개씩의 짝수와 홀수가 있습니다.

num_list = [5, 7, 8, 3]

def solution(num_list):
    odd_number = []
    even_number = []
    for i in num_list:
        if i%2 == 0:
            even_number.append(str(i))
        else: 
            odd_number.append(str(i))
    even = ''.join(even_number)
    odd = ''.join(odd_number)
    answer = int(even) + int(odd)
    return answer

print(solution(num_list))