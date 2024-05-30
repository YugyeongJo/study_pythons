# https://school.programmers.co.kr/learn/courses/30/lessons/181910

# 문제 설명
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string의 뒤의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# my_string은 숫자와 알파벳으로 이루어져 있습니다.
# 1 ≤ my_string의 길이 ≤ 1,000
# 1 ≤ n ≤ my_string의 길이

my_string = "ProgrammerS123"	
n = 11

def solution(my_string, n):
    answer = ''
    for i in range(1, n+1):
        answer = answer+my_string[-i]
    answer = answer[::-1]
    return answer

print(solution(my_string, n))