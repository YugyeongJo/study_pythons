# https://www.acmicpc.net/problem/2588

# 문제
# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

# 출력
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

#세 자리수 input 받기(두번째값 list로)
#첫번째 input 값 * 두번째 input값 각각의 자리수를 곱하기(3번모두)
#두번째 input int로 변환해서 곱셈값 출력

A = int(input())     #첫번째 숫자 int로 변환해서 input 받기
B = input()          #두번째 숫자 imput 받고, int 변환X(input받은 값을 각각 쪼개기 위해서)

temp_list = []       #두번째 숫자 쪼개기 위해 리스트화 

for i in range(len(B)):           #두번째 숫자 길이만큼 반복해서 각 자리의 숫자를 인덱스화
    temp_list.append(B[i])

first_multiply = A*int(temp_list[0])       #마지막자리수 곱하기
second_multiply = A*int(temp_list[1])      #두번째자리수 곱하기
third_multiply = A*int(temp_list[2])       #첫번째자리수 곱하기

B2 = int(B)                               #최종 곱한 값 산출을 위한 두번째 input값 int화 하기

fourth_multiply = A*B2                    #최종값 곱하기

print(third_multiply)                     #print
print(second_multiply)
print(first_multiply)
print(fourth_multiply)