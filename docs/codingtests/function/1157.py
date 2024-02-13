# https://www.acmicpc.net/problem/1157

# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 1) 모든 알파벳 대문자로 변환
# 2) 동일 알파벳 삭제 set
# 3) count활용해서 set으로 거른 알파벳의 갯수를 세줌
# 4) max를 활용해서 골라내기
# 5) if문 사용해서 max값이 여러개이면 ? 출력

A = list(input().upper())
B = list(set(A))

def function_name(A, B):
    index_list = []

    for i in range(len(B)):
        count_B = A.count(B[i])
        index_list.append(count_B)
    index_list_count = index_list.count(max(index_list))

    if index_list_count > 1:
        print("?")
    else:
        index_list_index = index_list.index(max(index_list))
        print(B[index_list_index])
    
    return 0 

function_name(A, B)