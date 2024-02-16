# https://school.programmers.co.kr/learn/courses/30/lessons/120903

# 문제 설명
# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

s1 = ["n", "omg"]
s2 = ["m", "dot"]	

def solution(s1, s2):
    answer = 0
    for i in s1:
        for x in s2:
            if i == x:
                answer += 1
    return answer

result = solution(s1, s2)
print(result)