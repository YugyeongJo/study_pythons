# https://www.acmicpc.net/problem/11382

# 문제
# 꼬마 정민이는 이제 A + B 정도는 쉽게 계산할 수 있다. 이제 A + B + C를 계산할 차례이다!

# 입력
# 첫 번째 줄에 A, B, C (1 ≤ A, B, C ≤ 1012)이 공백을 사이에 두고 주어진다.

# 출력
# A+B+C의 값을 출력한다.


#1줄로 input받기
#띄어쓰기 기준으로 글자 쪼개기
#쪼갠 글자를 각각 변수로 지정
#변수 총합 구하기


str = input().split()    #공백을 기준으로 input 쪼개기 .split()

A = str[0]               #각 쪼갠 list를 변수로 지정
B = str[1]
C = str[2]

add = int(A) + int(B) + int(C)        #지정해준 변수를 숫자로 변환하여 합산

print(add)