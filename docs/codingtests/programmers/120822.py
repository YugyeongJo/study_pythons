# https://school.programmers.co.kr/learn/courses/30/lessons/120822

# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

my_string = "jaron"

def solution(my_string):
    answer = my_string.reverse()
    return answer

# def solution(my_string):
#     list_my_string = list(my_string)
#     answer = list(reversed(list_my_string))
#     return answer

result = solution(my_string)
print(result)