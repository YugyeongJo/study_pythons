# https://school.programmers.co.kr/learn/courses/30/lessons/12940

# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.

n = 2
m = 5

def solution(n, m):
    answer = []
    n_a = []
    m_a = []
    for i in range(2, n+1):
        if n%i == 0 :
            n_a.append(i)
            
    for j in range(2, m+1):
        if m%j == 0 :
            m_a.append(j)
            
    for x in n_a:
        for y in m_a:
            if x == y:
                answer.append(x)
                break

    if len(answer) == 0:
        answer = [1]
    else:
        pass
    

    result = []
    for k in range(1, (n*m)+1):
        for z in range(1, (n*m)+1):
            if n*k != m*z:
                pass
            else:
                result.append(n*k)
                break
    answer.append(result[0])
    return answer

print(solution(n, m))