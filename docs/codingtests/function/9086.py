# https://www.acmicpc.net/problem/9086

# 문제
# 문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 한 줄에 하나의 문자열이 주어진다. 문자열은 알파벳 A~Z 대문자로 이루어지며 알파벳 사이에 공백은 없으며 문자열의 길이는 1000보다 작다.

# 출력
# 각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.

# 1) input받는 횟수 입력
# 2) for문 사용해서 횟수만큼 input 받기
# 3) 첫 글자와 마지막 글자 연속 출력하기

count = int(input())

def pop(count):        
    for i in range(count):
            str = list(input())
            first_str = str.pop(0)
            try:
                last_str = str.pop(-1)
            except:
                last_str = first_str
            str = first_str+last_str
            print(str)
    return 0

pop(count)
        