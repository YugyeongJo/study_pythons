# https://school.programmers.co.kr/learn/courses/30/lessons/120826

# 문제 설명
# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

my_string = "BCBdbe"		
letter = "B"

def solution(my_string, letter):
    my_string = list(my_string)
    while True:
        try:
            my_string.remove(letter)
        except:
            break
    answer = ''.join(my_string)
    return answer

result = solution(my_string, letter)
print(result)