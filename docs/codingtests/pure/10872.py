# https://www.acmicpc.net/problem/10872

# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

#N값 input 받기
#input받은 값부터 1까지 list화 시키기
#각 list 순서대로 곱하기

N = int(input())           

list_N = []

for i in range(N):
    list_N.append(N)
    N = N-1

M = 1
for count in range(len(list_N)):
    M = M*list_N[count]
    
print(M)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# n = input()

# count = 0
# N = []

# while count < n :
#     count += 1
#     N.append(count)
#     pass
# print(N)

# M = 1
# for i in range(n):
#     M = M * N[i]
#     pass





# ###### 제출필요