# https://www.acmicpc.net/problem/2444

# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

# 1) for 문 input 값 만큼 돌리기
# 2) 2×N-1 하는 갯수만큼 * print
# 3) *을 가운데에 출력? 

A = int(input())

blank = " "
star = "*"

def starprint(A, blank, star):
    for i in range(A):
        n = (A-1)-i
        m = 2*(i+1)-1
        printing = (blank*n) + (star*m)
        print(printing)
    for x in range(A):
        l = (2*A-1)-(2*(x+1))
        printing = (blank*(x+1)) + (star*l)
        print(printing)
    return 0 

answer = starprint(A, blank, star)