# https://www.acmicpc.net/problem/10809

# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

# 1) 알파벳 input받기
# + 중복값 제거 필요
# 2) A to Z, for문으로 일치 여부 비교
# 3) 비교한 값 list에 저장하기
# 4) list 출력

S = input()
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# alphabet = list(range(97,123))  # 아스키코드 활용

# 일치 여부 비교
def compare(S, alphabet):
    list_result = []
    for x in alphabet:
        if x in S:
            result = S.index(x)
            list_result.append(result)
        else : 
            list_result.append(-1)
    return list_result

answer = compare(S, alphabet)
print(*answer)


    

    
    