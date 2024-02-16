# https://school.programmers.co.kr/learn/courses/30/lessons/120836

# 문제 설명
# 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.

# 1) for문 사용해서 1~자기 자신까지 나누기
# 2) 나눴을때 나머지가 없는 숫자 append
# 3) len사용해서 append한 리스트의 갯수 세어주기

n = 100

def solution(n):
    list_number = []
    for i in range(1, n+1):
        if n%i == 0:
            list_number.append(i)
    answer = len(list_number)
    return answer

result = solution(n)
print(result)