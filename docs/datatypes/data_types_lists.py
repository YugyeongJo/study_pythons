numerics = [0, 1, 2, 3, 4]

# 사용 이유 : 값들에 모임을 쉽게 전달
# 숫자 5개 값들로 이루어진 리스트
list_numerics = [0, 1, 2, 3, 4]
# 문자 3개 값들로 이루어진 리스트
list_fruits = ["apple", "banana", "cherry"]
# 숫자와 문자 섞은 리스트 -> 우리는 쓰지 않는다
list_mixs = [0, 1, 2, 3, "apple", "banana",]

pass

# # 갯수를 알고 싶을때 len()을 사용
# len(list_numerics)
# 5
# len(list_mixs)
# 6

## for문 활용 후 다시 오기
pass

# index(색인, 위치값)
list_fruits = ["melon", "apple", "banana", "cherry"]
# ## index로 값 가져오기
# list_fruits[0]   # 단일 변수로 여김 1차원(행)
# 'melon'
# list_fruits[3]
# 'cherry'

## error 발생
# 'cherry'
# list_fruits[5]
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# IndexError: list index out of range
pass


# 1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?                  index 0
# A. Windows B. macOS C. Linux D. Chrome OS E. 기타            index 1
# 당신의 답변 : A


# 2. 주로 사용하는 프로그래밍 언어는 무엇인가요?                  index 2
# A. Python B. Java C. JavaScript D. C++ E. 기타               index 3
# 당신의 답변 : D

list_polls = [ 
            "1. 컴퓨터 운영체제에 대한 선호도는 어떠신가요?"
            ,"A. Windows B. macOS C. Linux D. Chrome OS E. 기타"
            ,"2. 주로 사용하는 프로그래밍 언어는 무엇인가요?"
            ,"A. Python B. Java C. JavaScript D. C++ E. 기타"
]

for str_content in list_polls:
    print("{}".format(str_content))
    pass
print("End program!")

# 설문 프로그램 만들기
for num_count in [0, 2]:
    # str_content = list_polls[num_count]
    # print("{}".format(str_content))
    str_question = list_polls[num_count]
    print("{}".format(str_question))

    str_answer = list_polls[num_count+1]
    print("{}".format(str_answer))
    
    input("당신의 답변(A-E를 번호로 입력) : ")
    print("-------------------------")

    pass
print("End program!")

# 



list_statistics = [0, 0, 0, 0, 0]       # 답항만큼 0을 넣어줌
for num_count in [0, 2]:
    # str_content = list_polls[num_count]
    # print("{}".format(str_content))
    str_question = list_polls[num_count]
    print("{}".format(str_question))

    str_answer = list_polls[num_count+1]
    print("{}".format(str_answer))

    str_question_result = input("당신에 답변(A-E를 순서에 맞게 번호로 입력) : ")
    num_question_result = int(str_question_result)        # 문자를 숫자로 변환
    index = num_question_result - 1 # index 위치값 적용
    list_statistics[index] = list_statistics[index] + 1
    
    print("-------------------------")
    pass

print("선호 답항 {}".format(list_statistics))
print("End program!")

# list 초기화 방식
list_fruits_primitive = ["melon", "apple", "banana", "cherry"]
turple_fruits = ("melon", "apple", "banana", "cherry")
list_fruits_constructor = list(("melon", "apple", "banana", "cherry"))

#type list인지 확인
type(list_fruits_primitive)
# <class 'list'>
type(list_fruits_constructor)
# <class 'list'>

#list append, remove, clear
# 삭제 대상이 해당 값이 있는 item
list_fruits_primitive.append('strawberry')
list_fruits_primitive.remove('apple')
list_fruits_constructor.remove('melon')
# 삭제 대상이 전체 item
list_fruits_primitive.clear()

pass