# https://school.programmers.co.kr/learn/courses/30/lessons/120908

# 문제 설명
# 문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

str1 = "AbcAbcA"
str2 = "AAA"	

def solution(str1, str2):
    if str2 in str1:
        answer = 1
    else : 
        answer = 2
    return answer

result = solution(str1, str2)
print(result)