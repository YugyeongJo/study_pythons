# https://www.acmicpc.net/problem/1001
# 문제
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 첫째 줄에 A-B를 출력한다.

A,B = map(int, input().split())

def pt(A,B):
    minus = A-B
    return minus

print(pt(A,B))