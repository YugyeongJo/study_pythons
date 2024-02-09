# https://www.acmicpc.net/problem/10869

# 문제
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

# 입력
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

# 출력
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

a,b = map(int, input().split())

def add(a, b):
    add = a+b
    return add

def minus(a, b):
    minus = a-b
    return minus

def multiple(a, b):
    multiple = a*b
    return multiple

def divide01(a, b):
    divide01 = a//b
    return divide01

def divide02(a, b):
    divide02 = a%b
    return divide02

answer01 = add(a, b)
answer02 = minus(a, b)
answer03 = multiple(a, b)
answer04 = divide01(a, b)
answer05 = divide02(a, b)

print(answer01)
print(answer02)
print(answer03)
print(answer04)
print(answer05)