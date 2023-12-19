# function에 들어가는 값들
# 변수를 사용한 function
# 변수의 값은 호출할때 할당됨
def add(num_first, num_second) :
    sum = num_first + num_second
    return sum  # 상수 대신 변수 사용

if__name__ ==  "__main__":
    num_sum = add(5, 4) 
    print("add()의 return 결과 : {}".format(num_sum))
    num_sum = add(6, 10) 
    print("add()의 return 결과 : {}".format(num_sum))

# # 상수 parameters 사용
# def add(num_first, num_second) :
#     sum = num_first + num_second
#     return sum  # 상수 대신 변수 사용
# num_sum = add(5, 4) 
# print("add()의 return 결과 : {}".format(num_sum))
# num_sum = add(6, 10) 
# print("add()의 return 결과 : {}".format(num_sum))

# 내 점수 넣으면 학점이 나오는 function
# 
def score(my_score) :          # 자신을 불렀을 때 값들 할당(순서 매칭)
    my_grade = ''
    if my_score >= 90 :
        my_grade = 'A'
    elif my_score > 80 :
        my_grade = 'B'
    else :
        my_grade = 'C'
    return my_grade

if__name__ ==  "__main__":
    # str_grade = score(99)         # 호출 시 값들이 넘어감(순서 매칭)
    # print("당신의 학점은 {}입니다.".format(str_grade))
    my_score = 88
    str_grade = score(my_score)
    print("당신의 학점은 {}입니다.".format(str_grade))