# https://school.programmers.co.kr/learn/courses/30/lessons/120814

# 문제 설명
# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.
import math
n = 15

def solution(n):
    if n > 7 :
        out = n/7
        answer = math.ceil(out)
    else : 
        answer = 1
    return answer

result = solution(n)
print(result)