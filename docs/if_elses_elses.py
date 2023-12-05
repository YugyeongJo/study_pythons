# 기본 if - elif - else 구문
if True : 
    pass
elif True : 
    pass
else : 
    pass

# 문자 비교
str_name = "yugyeong jo"

## 질문 형식(condition) : 변수 + 부등호 + 기준값
# 문자에 대한 긍정으로 질문
if str_name == "yugyeong jo" :
    pass
print("name is {}.".format(str_name))

# 문자에 대한 부정으로 질문
if str_name != "yugyeong jo" :
    pass
    print("name is not {}.".format(str_name))

## if - else
# num_first >= 4 -> True : 큼, False : 작음
num_first = 5
# if num_first >= 4 :        # 무조건 둘 중 하나 표현해야하는 경우 사용
if num_first >= 6 : 
    pass        # condition이 True이면 실행되는 부분
    print("{}는 6보다 크다." .format(num_first))
else : 
    pass        # condition이 False이면 실행되는 부분
    print("{}는 6보다 작다." .format(num_first))

## if - elif - else 
# 점수에 따른 표시
# 90점 이상 : A, 80점 초과 : B, 나머지는 F
my_score = 90

if my_score >= 90 :            # 90점 이상 : A
    pass
    print("{}점은 90점 이상이기 때문에 A입니다.".format(my_score))
elif my_score > 80 :           # 80점 초과 : B
    pass
    print("{}점은 80점 초과이기 때문에 B입니다.".format(my_score))
else :           # 나머지 : F
    pass
    print("{}점은 80점 이하이기 때문에 F입니다.".format(my_score))
print("End Program!")